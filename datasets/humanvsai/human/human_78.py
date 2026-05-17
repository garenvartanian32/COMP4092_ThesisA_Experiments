def validate(parsed_args):
    parsed_args = vars(parsed_args)
    data_set = parsed_args['dataset']
    expectations_config_file = parsed_args['expectations_config_file']
    expectations_config = json.load(open(expectations_config_file))
    if parsed_args["evaluation_parameters"] is not None:
        evaluation_parameters = json.load(
            open(parsed_args["evaluation_parameters"]))
    else:
        evaluation_parameters = None
    # Use a custom dataasset module and class if provided. Otherwise infer from the config.
    if parsed_args["custom_dataset_module"]:
        sys.path.insert(0, os.path.dirname(
            parsed_args["custom_dataset_module"]))
        module_name = os.path.basename(
            parsed_args["custom_dataset_module"]).split('.')[0]
        custom_module = __import__(module_name)
        dataset_class = getattr(
            custom_module, parsed_args["custom_dataset_class"])
    elif "data_asset_type" in expectations_config:
        if expectations_config["data_asset_type"] == "Dataset" or expectations_config["data_asset_type"] == "PandasDataset":
            dataset_class = PandasDataset
        elif expectations_config["data_asset_type"].endswith("Dataset"):
            logger.info("Using PandasDataset to validate dataset of type %s." % expectations_config["data_asset_type"])
            dataset_class = PandasDataset
        elif expectations_config["data_asset_type"] == "FileDataAsset":
            dataset_class = FileDataAsset
        else:
            logger.critical("Unrecognized data_asset_type %s. You may need to specifcy custom_dataset_module and custom_dataset_class." % expectations_config["data_asset_type"])
            return -1
    else:
        dataset_class = PandasDataset
    if issubclass(dataset_class, Dataset):
        da = read_csv(data_set, expectations_config=expectations_config,
                    dataset_class=dataset_class)
    else:
        da = dataset_class(data_set, config=expectations_config)
    result = da.validate(
        evaluation_parameters=evaluation_parameters,
        result_format=parsed_args["result_format"],
        catch_exceptions=parsed_args["catch_exceptions"],
        only_return_failures=parsed_args["only_return_failures"],
    )
    print(json.dumps(result, indent=2))
    return result['statistics']['unsuccessful_expectations']