from datetime import datetime, timedelta


def find_free_slots(busy_schedule, work_start, work_end):
    '''Функция поиска свободных слотов по N минут в диапазоне заданного
     времени, с учетом переданных нерабочих часов.
    '''
    work_start = datetime.strptime(work_start, '%H:%M')
    work_end = datetime.strptime(work_end, '%H:%M')
    appointment_interval = timedelta(minutes=30)

    busy_times = []
    for appointment in busy_schedule:
        start_time = datetime.strptime(appointment['start'], '%H:%M')
        stop_time = datetime.strptime(appointment['stop'], '%H:%M')
        busy_times.append((start_time, stop_time))
    busy_times.append((work_end, work_end))

    current_time = work_start
    free_slots = []
    i = 0
    while current_time < work_end:

        busy_time = busy_times[i]
        appointmnet_end = current_time + appointment_interval
        if appointmnet_end <= busy_time[0]:
            free_slots.append({'start': current_time, 'stop': appointmnet_end})
            current_time = appointmnet_end
        else:
            current_time = busy_time[1]
            i += 1

    return free_slots


if __name__ == '__main__':

    busy = [
        {'start': '10:30',
         'stop': '10:50'
         },
        {'start': '18:40',
         'stop': '18:50'
         },
        {'start': '14:40',
         'stop': '15:50'
         },
        {'start': '16:40',
         'stop': '17:20'
         },
        {'start': '20:05',
         'stop': '20:20'
         }]

    free_slots = find_free_slots(busy_schedule=busy,
                                 work_start='09:00',
                                 work_end='21:00')

    for slot in free_slots:
        print(f"Free slot: {slot['start'].strftime('%H:%M')}"
              f" - {slot['stop'].strftime('%H:%M')}")


