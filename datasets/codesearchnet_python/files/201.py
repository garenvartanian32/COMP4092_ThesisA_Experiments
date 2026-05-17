def pprint(self, num=10):
        """
        Print the first num elements of each RDD generated in this DStream.

        @param num: the number of elements from the first will be printed.
        """
        def takeAndPrint(time, rdd):
            taken = rdd.take(num + 1)
            print("-------------------------------------------")
            print("Time: %s" % time)
            print("-------------------------------------------")
            for record in taken[:num]:
                print(record)
            if len(taken) > num:
                print("...")
            print("")

        self.foreachRDD(takeAndPrint)