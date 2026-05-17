def iter_previous(self, iter):
        prev_iter = iter.copy()
        success = super(TreeModel, self).iter_previous(prev_iter)
        if success:
            return prev_iter