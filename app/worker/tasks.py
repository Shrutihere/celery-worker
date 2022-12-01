from celery import Task
from dateutil.rrule import rrulestr, rrule

from .schedule import (
    CancelSchedule,
    TaskScheduler
)

_DATE_FORMAT = TaskScheduler.DATE_FORMAT


class RepeatTask(Task):
    """Base task for executing repeated tasks."""

    def __call__(self, *args, **kwargs):
        # Pop out custom keyword arguments added during scheduling and
        # previous run so as not to pollute the task function's
        # namespace.
        # scheduled_task_id = kwargs.pop('scheduled_task_id')
        rrule_string = kwargs.pop('rrule_string')
        _first_eta = kwargs.pop('first_eta')
        _eta = kwargs.pop('eta')
        _until = kwargs.pop('until')

        first_eta = TaskScheduler.strptime(_first_eta)
        eta = TaskScheduler.strptime(_eta)
        until = TaskScheduler.strptime(_until)
        # scheduled_task = ScheduledTask.objects.get(pk=scheduled_task_id)

        # # If the task been manually set as ScheduledTask.STATUS_CANCELLED,
        # # stop the execution.
        # if scheduled_task.status == ScheduledTask.STATUS_CANCELLED:
        #     return

        # scheduled_task.save_status(ScheduledTask.STATUS_RUNNING)
        # ScheduledTaskRunLog.objects.create(task_id=self.request.id,
        #                                    scheduled_task=scheduled_task)

        # If a CancelSchedule exception is raied by the function,
        # cancel the schedule and exit.
        try:
            result = super(RepeatTask, self).__call__(*args, **kwargs)
        except CancelSchedule:
            # TaskScheduler.cancel(scheduled_task_id=scheduled_task.id)
            return
        # else:
        #     scheduled_task.save_status(ScheduledTask.STATUS_SUCCESS)

        # If rrule string is not specified, assume it to be a one time
        # task.
        if not rrule_string:
            return result

        # Preserve the start and end of rrule cycle.
        # rrule_ = rrulestr(rrule_string).replace(dtstart=first_eta,
                                                # until=until)

        rrule_ = rrule(
            freq=rrule_string["freq"],
            dtstart=first_eta,
            interval=rrule_string["interval"],
            wkst=rrule_string["wkst"],
            until=until,
            bysetpos=rrule_string["bysetpos"],
            bymonth=rrule_string["bymonth"],
            bymonthday=rrule_string["bymonthday"],
            byyearday=rrule_string["byyearday"],
            byweekday=rrule_string["byweekday"],
            byweekno=rrule_string["byweekno"],
            byhour=rrule_string["byhour"],
            byminute=rrule_string["byminute"],
            bysecond=rrule_string["bysecond"],

        )

        next_eta = TaskScheduler.calculate_next_eta(rrule_=rrule_,
                                                    current_eta=eta)
        # If rrule does not return an ETA, assume it to be the end of
        # schedule and exit.
        if not next_eta:
            return result

        # Add custom keyword arguments again for the next run.
        kwargs.update({
            # 'scheduled_task_id': scheduled_task_id,
            'rrule_string': rrule_string,
            'first_eta': _first_eta,
            'eta': TaskScheduler.strftime(next_eta),
            'until': TaskScheduler.strftime(until),
        })

        self.apply_async(eta=next_eta, args=args, kwargs=kwargs)
        return result