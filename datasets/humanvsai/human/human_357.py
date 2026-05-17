def sample(self, trials: int) -> np.ndarray:
        # TODO: Can we do this within backend?
        probs = np.real(bk.evaluate(self.probabilities()))
        res = np.random.multinomial(trials, probs.ravel())
        res = res.reshape(probs.shape)
        return res