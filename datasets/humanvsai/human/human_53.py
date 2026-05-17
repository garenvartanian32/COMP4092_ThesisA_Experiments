def remove(self):
        
        title = '%s.remove' % self.__class__.__name__
    
    # request bucket delete 
        self.s3.delete_bucket(self.bucket_name)
    # return confirmation
        exit_msg = '%s collection has been removed from S3.' % self.bucket_name
        return exit_msg