import argparse
import csv
import glob
import io
import lzma
import os
import zipfile

import rows


class NotNullTextWrapper(io.TextIOWrapper):

    def read(self, *args, **kwargs):
        data = super().read(*args, **kwargs)
        return data.replace('\x00', '')

    def readline(self, *args, **kwargs):
        data = super().readline(*args, **kwargs)
        return data.replace('\x00', '')


class PtBrDateField(rows.fields.DateField):
    INPUT_FORMAT = '%d/%m/%Y'


def open_compressed_file(filename, encoding):
    zf = zipfile.ZipFile(filename)
    assert len(zf.filelist) == 1
    compressed = zf.filelist[0]
    raw_fobj = zf.open(compressed.filename)
    return NotNullTextWrapper(raw_fobj, encoding=encoding)


def convert_spend(row):
    new = {slug(key): value.strip() if value is not None else value
           for key, value in row.items()}

    new['data_pagamento_original'] = None
    try:
        new['data_pagamento'] = rows.fields.DateField.serialize(
            PtBrDateField.deserialize(new['data_pagamento'])
        )
    except ValueError:
        new['data_pagamento_original'] = new['data_pagamento']
        new['data_pagamento'] = None

    new['valor'] = new['valor'].replace('.', '').replace(',', '.')

    return new


def convert_transfer(row):
    new = {slug(key): value.strip() if value is not None else value
           for key, value in row.items()}

    if new['valor_parcela'] is not None:
        new['valor_parcela'] = new['valor_parcela'].replace(',', '')

    return new


def read_files(filenames, extract_row):
    for filename in filenames:
        parts = filename.replace('.zip', '').split('-')
        year, month = parts[-2], parts[-1]

        # Detect the "CSV" dialect
        text_fobj = open_compressed_file(filename, input_encoding)
        sample = text_fobj.read(256 * 1024)  # sample size: 256 KiB
        dialect = discover_dialect(sample.encode('utf-8'), 'utf-8')

        # Open file again, since ZipFile does not allow seek
        text_fobj = open_compressed_file(filename, input_encoding)
        for index, row in enumerate(csv.DictReader(text_fobj, dialect=dialect)):
            data = extract_row(row)
            data['ano'], data['mes'] = year, month
            yield data


def merge_files(filenames, input_encoding, output_filename, output_encoding,
        extract_row, print_stats, print_interval=10000):

    with lzma.LZMAFile(output_filename, mode='wb', format=lzma.FORMAT_XZ) as xz_fobj, \
        io.TextIOWrapper(xz_fobj, encoding='utf-8') as output_fobj:
        # TODO: run extractions in parallel
        data = read_files(filenames, extract_row)

        first_row = next(data)
        writer = csv.DictWriter(output_fobj, fieldnames=first_row.keys())
        writer.writeheader()
        writer.writerow(first_row)

        for index, row in enumerate(data, start=2):
            writer.writerow(row)
            if index % print_interval == 0:
                print_stats(index, row)


def print_stats(index, row):
    print(f'{row["ano"]}-{row["mes"]} {index:012d}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('type', choices=['gastos-diretos', 'transferencias'])
    args = parser.parse_args()

    discover_dialect = rows.plugins.csv.discover_dialect
    slug = rows.plugins.utils.slug
    input_encoding = 'iso-8859-1'
    filenames = sorted(glob.glob(f'download/{args.type}-*.zip'))
    output_filename = f'output/{args.type}.csv.xz'
    output_encoding = 'utf-8'
    if not os.path.exists('output'):
        os.mkdir('output')
    convert_function = {'transferencias': convert_transfer,
                        'gastos-diretos': convert_spend, }[args.type]
    merge_files(filenames, input_encoding, output_filename,
                output_encoding, convert_function, print_stats)
