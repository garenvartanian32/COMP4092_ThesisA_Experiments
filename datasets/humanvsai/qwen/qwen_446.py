def run_all_evals(models, treebanks, out_file, check_parse, print_freq_tasks):
    for lang in models:
        print(f'Starting evaluation for {lang}')
        for model in models[lang]:
            print(f'Evaluating model {model} on {lang}')
            for treebank in treebanks[lang]:
                print(f'Evaluating {model} on {treebank}')
                result = evaluate_model(model, treebank, check_parse)
                if print_freq_tasks:
                    print(f'Result for {model} on {treebank}: {result}')
                with open(out_file, 'a') as f:
                    f.write(f'{lang}\t{model}\t{treebank}\t{result}\n')
    print('All evaluations completed.')
models = {'English': ['model1', 'model2'], 'Spanish': ['model3']}
treebanks = {'English': ['treebank1', 'treebank2'], 'Spanish': ['treebank3']}
out_file = 'evaluation_results.txt'
check_parse = True
print_freq_tasks = True