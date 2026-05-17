def request_output(self, table, outtype):
        job_types = ["CSV", "DataSet", "FITS", "VOTable"]
        assert outtype in job_types
        params = {"tableName": table, "type": outtype}
        r = self._send_request("SubmitExtractJob", params=params)
        job_id = int(self._parse_single(r.text, "long"))
        return job_id