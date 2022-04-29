from mrjob.job import MRJob


Class Bacon_count(MRJob):
def mapper(self, _, line):
    for word in line.split():
        if word.lower() == "bacon":
            yield "bacon", 1
