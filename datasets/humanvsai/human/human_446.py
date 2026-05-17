def run_all_evals(models, treebanks, out_file, check_parse, print_freq_tasks):
    print_header = True
    for tb_lang, treebank_list in treebanks.items():
        print()
        print("Language", tb_lang)
        for text_path in treebank_list:
            print(" Evaluating on", text_path)
            gold_path = text_path.parent / (text_path.stem + '.conllu')
            print("  Gold data from ", gold_path)
            # nested try blocks to ensure the code can continue with the next iteration after a failure
            try:
                with gold_path.open(mode='r', encoding='utf-8') as gold_file:
                    gold_ud = conll17_ud_eval.load_conllu(gold_file)
                for nlp, nlp_loading_time, nlp_name in models[tb_lang]:
                    try:
                        print("   Benchmarking", nlp_name)
                        tmp_output_path = text_path.parent / str('tmp_' + nlp_name + '.conllu')
                        run_single_eval(nlp, nlp_loading_time, nlp_name, text_path, gold_ud, tmp_output_path, out_file,
                                        print_header, check_parse, print_freq_tasks)
                        print_header = False
                    except Exception as e:
                        print("    Ran into trouble: ", str(e))
            except Exception as e:
                print("   Ran into trouble: ", str(e))