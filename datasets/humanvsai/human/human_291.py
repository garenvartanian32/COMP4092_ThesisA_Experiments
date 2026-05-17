def _update_structure_from_config(self, structure):
        # We initiate a variable which will map what we have to replace `ouput` to.
        # Indeed, as we allow the user to change directory names directly from the
        # configuration, here we initiate what we have to replace `output/` with.
        to_replace_base_map = {"output/": PyFunceble.OUTPUTS["parent_directory"]}
        # We map the replacement of other directories.
        to_replace_map = {
            #########################################################################
            #            The following part is there for historical reason.         #
            #########################################################################
            # We get the replacement of the HTTP_Analytic directory from the
            # configuration file.
            "HTTP_Analytic/": PyFunceble.OUTPUTS["analytic"]["directories"]["parent"],
            # We get the replacement of the HTTP_Analytic/ACTIVE directory from the
            # configuration file.
            "HTTP_Analytic/ACTIVE/": PyFunceble.OUTPUTS["analytic"]["directories"][
                "parent"
            ]
            + PyFunceble.OUTPUTS["analytic"]["directories"]["up"],
            "HTTP_Analytic/POTENTIALLY_ACTIVE/": PyFunceble.OUTPUTS["analytic"][
                "directories"
            ]["parent"]
            + PyFunceble.OUTPUTS["analytic"]["directories"]["potentially_up"],
            # We get the replacement of the HTTP_Analytic/POTENTIALLY_INACTIVE directory
            # from the configuration file.
            "HTTP_Analytic/POTENTIALLY_INACTIVE/": PyFunceble.OUTPUTS["analytic"][
                "directories"
            ]["parent"]
            + PyFunceble.OUTPUTS["analytic"]["directories"]["potentially_down"],
            #########################################################################
            #             The previous part is there for historical reason.         #
            #########################################################################
            # We get the replacement of the Analytic directory from the
            # configuration file.
            "Analytic/": PyFunceble.OUTPUTS["analytic"]["directories"]["parent"],
            # We get the replacement of the Analytic/ACTIVE directory from the
            # configuration file.
            "Analytic/ACTIVE/": PyFunceble.OUTPUTS["analytic"]["directories"]["parent"]
            + PyFunceble.OUTPUTS["analytic"]["directories"]["up"],
            "Analytic/POTENTIALLY_ACTIVE/": PyFunceble.OUTPUTS["analytic"][
                "directories"
            ]["parent"]
            + PyFunceble.OUTPUTS["analytic"]["directories"]["potentially_up"],
            # We get the replacement of the Analytic/POTENTIALLY_INACTIVE directory
            # from the configuration file.
            "Analytic/POTENTIALLY_INACTIVE/": PyFunceble.OUTPUTS["analytic"][
                "directories"
            ]["parent"]
            + PyFunceble.OUTPUTS["analytic"]["directories"]["potentially_down"],
            # We get the replacement of the Analytic/SUSPICIOUS directory
            # from the configuration file.
            "Analytic/SUSPICIOUS/": PyFunceble.OUTPUTS["analytic"]["directories"][
                "parent"
            ]
            + PyFunceble.OUTPUTS["analytic"]["directories"]["suspicious"],
            # We get the replacement of the domains directory from the
            # configuration file.
            "domains/": PyFunceble.OUTPUTS["domains"]["directory"],
            # We get the replacement of the domains/ACTIVE directory from the
            # configuration file.
            "domains/ACTIVE/": PyFunceble.OUTPUTS["domains"]["directory"]
            + PyFunceble.STATUS["official"]["up"],
            # We get the replacement of the domains/INACTIVE directory from the
            # configuration file.
            "domains/INACTIVE/": PyFunceble.OUTPUTS["domains"]["directory"]
            + PyFunceble.STATUS["official"]["down"],
            # We get the replacement of the domains/INVALID directory from the
            # configuration file.
            "domains/INVALID/": PyFunceble.OUTPUTS["domains"]["directory"]
            + PyFunceble.STATUS["official"]["invalid"],
            # We get the replacement of the domains/VALID directory from the
            # configuration file.
            "domains/VALID/": PyFunceble.OUTPUTS["domains"]["directory"]
            + PyFunceble.STATUS["official"]["valid"],
            # We get the replacement of the hosts directory from the
            # configuration file.
            "hosts/": PyFunceble.OUTPUTS["hosts"]["directory"],
            # We get the replacement of the hosts/ACTIVE directory from the
            # configuration file.
            "hosts/ACTIVE/": PyFunceble.OUTPUTS["hosts"]["directory"]
            + PyFunceble.STATUS["official"]["up"],
            # We get the replacement of the hosts/INACTIVE directory from the
            # configuration file.
            "hosts/INACTIVE/": PyFunceble.OUTPUTS["hosts"]["directory"]
            + PyFunceble.STATUS["official"]["down"],
            # We get the replacement of the hosts/INVALID directory from the
            # configuration file.
            "hosts/INVALID/": PyFunceble.OUTPUTS["hosts"]["directory"]
            + PyFunceble.STATUS["official"]["invalid"],
            # We get the replacement of the hosts/VALID directory from the
            # configuration file.
            "hosts/VALID/": PyFunceble.OUTPUTS["hosts"]["directory"]
            + PyFunceble.STATUS["official"]["valid"],
            # We get the replacement of the json directory from the
            # configuration file.
            "json/": PyFunceble.OUTPUTS["json"]["directory"],
            # We get the replacement of the json/ACTIVE directory from the
            # configuration file.
            "json/ACTIVE/": PyFunceble.OUTPUTS["json"]["directory"]
            + PyFunceble.STATUS["official"]["up"],
            # We get the replacement of the json/INACTIVE directory from the
            # configuration file.
            "json/INACTIVE/": PyFunceble.OUTPUTS["json"]["directory"]
            + PyFunceble.STATUS["official"]["down"],
            # We get the replacement of the json/INVALID directory from the
            # configuration file.
            "json/INVALID/": PyFunceble.OUTPUTS["json"]["directory"]
            + PyFunceble.STATUS["official"]["invalid"],
            # We get the replacement of the json/VALID directory from the
            # configuration file.
            "json/VALID/": PyFunceble.OUTPUTS["json"]["directory"]
            + PyFunceble.STATUS["official"]["valid"],
            # We get the replacement of the logs directory from the
            # configuration file.
            "logs/": PyFunceble.OUTPUTS["logs"]["directories"]["parent"],
            # We get the replacement of the logs/percentage directory from the
            # configuration file.
            "logs/percentage/": PyFunceble.OUTPUTS["logs"]["directories"]["parent"]
            + PyFunceble.OUTPUTS["logs"]["directories"]["percentage"],
            # We get the replacement of the splited directory from the
            # configuration file.
            "splited/": PyFunceble.OUTPUTS["splited"]["directory"],
        }
        # We initiate the variable which will be used for the structure
        # update.
        to_replace = {}
        for mapped, declared in to_replace_map.items():
            # We loop through the declared mad.
            # We fix the path of the declared.
            declared = Directory(declared).fix_path()
            # print('dec', declared, 'map', mapped)
            # And we update our data.
            to_replace.update({mapped: declared})
        to_replace_base = {}
        for mapped, declared in to_replace_base_map.items():
            # We loop through the declared mad.
            # We fix the path of the declared.
            declared = Directory(declared).fix_path()
            # And we update our data.
            to_replace_base.update({mapped: declared})
        # We perform the replacement of the base directory.
        structure = Dict(structure).rename_key(to_replace_base)
        # We perform the replacement of every subdirectories.
        structure[PyFunceble.OUTPUTS["parent_directory"]] = Dict(
            structure[PyFunceble.OUTPUTS["parent_directory"]]
        ).rename_key(to_replace)
        try:
            # We try to save the structure into the right path.
            Dict(structure).to_json(self.structure)
        except FileNotFoundError:
            # But if we get a FileNotFoundError exception,
            # We create the directory where the directory structure should be saved.
            PyFunceble.mkdir(
                PyFunceble.directory_separator.join(
                    self.structure.split(PyFunceble.directory_separator)[:-1]
                )
            )
            # And we retry to save the structure into the right path.
            Dict(structure).to_json(self.structure)
        # We finaly return the new structure in case it's needed for other logic.
        return structure