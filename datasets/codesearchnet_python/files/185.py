def train(cls, rdd, k=10, maxIterations=20, docConcentration=-1.0,
              topicConcentration=-1.0, seed=None, checkpointInterval=10, optimizer="em"):
        """Train a LDA model.

        :param rdd:
          RDD of documents, which are tuples of document IDs and term
          (word) count vectors. The term count vectors are "bags of
          words" with a fixed-size vocabulary (where the vocabulary size
          is the length of the vector). Document IDs must be unique
          and >= 0.
        :param k:
          Number of topics to infer, i.e., the number of soft cluster
          centers.
          (default: 10)
        :param maxIterations:
          Maximum number of iterations allowed.
          (default: 20)
        :param docConcentration:
          Concentration parameter (commonly named "alpha") for the prior
          placed on documents' distributions over topics ("theta").
          (default: -1.0)
        :param topicConcentration:
          Concentration parameter (commonly named "beta" or "eta") for
          the prior placed on topics' distributions over terms.
          (default: -1.0)
        :param seed:
          Random seed for cluster initialization. Set as None to generate
          seed based on system time.
          (default: None)
        :param checkpointInterval:
          Period (in iterations) between checkpoints.
          (default: 10)
        :param optimizer:
          LDAOptimizer used to perform the actual calculation. Currently
          "em", "online" are supported.
          (default: "em")
        """
        model = callMLlibFunc("trainLDAModel", rdd, k, maxIterations,
                              docConcentration, topicConcentration, seed,
                              checkpointInterval, optimizer)
        return LDAModel(model)