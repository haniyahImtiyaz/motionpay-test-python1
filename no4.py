import datetime

def checkCuti(cuti_bersama, join_date, cuti_date, duration):
    join_date = datetime.datetime.strptime(join_date, '%Y-%m-%d')
    cuti_date = datetime.datetime.strptime(cuti_date, '%Y-%m-%d')
    max_duration = 3

    # allowed only after 180 days
    diff = cuti_date - join_date
    if(diff.days < 180 ):
        return {
            'status': False,
            'reason': 'Karena belum 180 hari sejak tanggal join karyawan'
        }

    if(duration > max_duration):
        return {
            'status': False,
            'reason': f'Karena max cuti pribadi adalah {max_duration} hari berurutan'
        }

    cuti_kantor = 14
    cuti_pribadi = cuti_kantor - cuti_bersama
    
    # in first year
    if(cuti_date.year == join_date.year):
        start_date = join_date + datetime.timedelta(days = 180)
        last_date = datetime.datetime.strptime(f'12-31-{join_date.year}', '%m-%d-%Y')
        max_duration = int((last_date - start_date).days / 365 * cuti_pribadi)

    if(duration > max_duration):
        return {
            'status': False,
            'reason': f'Karena hanya boleh mengambil {max_duration} hari cuti'
        }

    return {
        'status': True
    }

# main process
cuti_bersama = input('Jumlah Cuti Bersama: ')
join_date = input('Tanggal join karyawan: ')
cuti_date = input('Tanggal rencana cuti: ')
duration = input('Durasi cuti (hari): ')

result = checkCuti(int(cuti_bersama), join_date, cuti_date, int(duration))
for text in result.values():
    print(text)

