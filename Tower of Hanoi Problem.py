class Tower:

    def __init__(self):

        self.terminate = 1

    def printMove(self, disc, source, destination):

        print("Move disk", disc, "from source", source, "to destination", destination)

    def move(self, disc, source, destination, auxiliary):

        if disc == self.terminate:

            self.printMove(1, source, destination)

        else:

            self.move(disc - 1, source, auxiliary, destination)

            self.printMove(disc, source, destination)

            self.move(disc - 1, auxiliary, destination, source)


t = Tower();

t.move(3, 'A', 'B', 'C')