import logging
from threading import Thread
from .mikecrm import Mikecrm

class MikeBrush():
    def __init__(self, target, proxys, count):
        '''
        Brush for voting on mike
        :param target: {"page":"", "data":""}
        :param proxys: Queue for {"type":"", "ip":"", "port":00}
        :param count: number of threadings
        '''
        self.target = target
        self.proxys = proxys
        self.count = count
        self.total = 0
        self.votes = 0

    def brush_schedule(self, index):
        proxys = self.proxys
        brush = Mikecrm(**self.target)
        logging.info('Brush thead-%d : task started!' % index)
        while not proxys.empty():
            proxy = proxys.get_nowait()
            self.total += 1
            if brush.set_proxy(*proxy).submit():
                self.votes += 1
            logging.info('Current successes count is %d / %d' % (self.votes, self.total))
        logging.info('Brush thead-%d : task complete!' % index)

    def run(self, block=True):
        tasks = []
        for index in range(self.count):
            task = Thread(name='Theading-%d'%(index+1), target=self.brush_schedule, args=(index,))
            tasks.append(task)
            task.start()
        logging.info('Brush tasks all started!')
        if block:
            for task in tasks:
                task.join()
            logging.info('Brush tasks all complete!')
