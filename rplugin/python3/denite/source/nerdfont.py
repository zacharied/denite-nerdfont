from .base import Base
from denite.util import globruntime

class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'nerdfont'
        self.kind = 'word'

        # TODO Autodownload
        self.file_index = globruntime(vim.eval('&runtimepath'), 'autoload/nerdfont-denite/icons.csv')[0]

    def gather_candidates(self, context):
        candidates = [ ]
        with open(self.file_index, "r") as f:
            for l in f.readlines():
                pair = l.strip().split(',')
                candidates.append({ 'word': pair[1] + ':' + pair[0], 'action__text': pair[1]})
        return candidates
