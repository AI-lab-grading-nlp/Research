import json

rubric = {}

rubric['#algorithms'] = 'Identifies an appropriate algorithmic strategy and justifies the choice; accurately implements or interprets an algorithm, using code if appropriate, with detailed, clear, and efficient steps; (when applicable) provides thorough explanation of code (e.g. comments); (when applicable) effectively implements and explains a complex, sophisticated algorithm.'
rubric['#confidenceintervals'] = 'Accurately interprets the meaning of a confidence interval with well justified reasoning; (when applicable) accurately calculates a confidence interval for a given sample and population characteristic with clear and detailed steps; accurately applies a confidence interval for estimating population parameter with an explained interpretation; (when applicable) applies confidence intervals to a sophisticated, complex inference problem.'
rubric['#correlation'] = 'Accurately applies correlation to interpret the relationship between variables with clear and appropriately detailed explanation; recognizes and effectively explains the difference between correlation and causation within the given context; (when applicable) computes or interprets a measure of correlation and provides a clear and detailed and explanation within the given context; (when applicable) identifies nontrivial extraneous variables that could be the underlying cause of the correlation and effectively explains the potential links.'
rubric['#deduction'] = 'Accurately applies and analyzes deductive reasoning with clear and detailed explanation; (when applicable) accurately identifies premises and conclusions and justifies the identification; (when applicable) provides a detailed, well-justified evaluation of the relationships among propositions with easy to follow steps; (when applicable) accurately distinguishes between validity and soundness and explains the meaning of each in the given context; provides a detailed, well justified evaluation of the validity or soundness; (when applicable) accurately and effectively applies deductive techniques to a complex, sophisticated derivation.'
rubric['#descriptivestats'] = 'Chooses an appropriate descriptive statistic and justifies the choice; accurately calculates a descriptive statistic with clear detailed steps; provides a well reasoned and justified interpretation of the statistic; (when applicable) correctly creates a histogram for the data and provides detailed interpretation; (when applicable) applies multiple descriptive statistics to create a robust analysis of the data.'
rubric['#distributions'] = 'Accurately identifies an appropriate distribution in the given context and justifies the choice; accurately describes features or characteristics of a distribution, including relevant calculations, with an appropriate level of detail; (when applicable) correctly considers the effects of the underlying distribution when making inferences from samples, including required assumptions, and clearly explains the consequences and limitations; (when applicable) accurately recognizes when regression to the mean applies in a given context and describes measures to mitigate the effect.'
rubric['#modeling'] = 'Accurately identifies an existing model that can describe a system, explain patterns in empirical data, test a theory, or make predictions and provides a clear justification for the choice; accurately determines the relevant aspects of a model in a given context and provides a clear justification for the choice; (when applicable) effectively develops a model appropriate to the context and provides a clear, detailed explanation; (when applicable) accurately interprets and clearly explains the results or implications of applying a model; (when applicable) accurately evaluates the effectiveness of an application of a model and provides a well-supported critique or suggests a non-trivial improvement.'
rubric['#probability'] = 'Accurately applies appropriate probabilities with well justified reasoning; accurately interprets probabilities with well justified reasoning; (when applicable) accurately distinguishes between different interpretations of probability and provides a detailed explanation; (when applicable) accurately calculates an appropriate probability with clear detailed steps; (when applicable) accurately and effectively applies an appropriate probability or interprets a probability in a complex or sophisticated context.'
rubric['#regression'] = 'Accurately constructs or interprets a regression model with a well-justified explanation of the relation between dependent and independent variables; (when applicable) accurately computes or interprets the regression equation with clear and detailed explanation; (when applicable) accurately computes or interprets the coefficient of determination with clear and detailed explanation; (when applicable) accurately uses a regression model for prediction and effectively explains the result in the given context; (when applicable) effectively implements and interprets a complex, sophisticated regression model.'
rubric['#significance'] = 'Accurately applies or interprets an appropriate significance test or measure of significance with well justified reasoning; (when applicable) accurately distinguishes between type I and type II errors and explains the potential consequences; (when applicable) accurately distinguishes between practical and statistical significance and explains the difference within a given context; (when applicable) accurately and effectively calculates or interprets the results of a significance test or measure in a subtle or complex scenario.'



def make_rubric_components(big_rubric):
    big_rubric = big_rubric.replace('(when applicable) ', '')
    big_rubric = big_rubric.replace('\n', '')
    big_rubric = " ".join(big_rubric.split())
    rubric_lst = big_rubric.split(';')

    return rubric_lst

rubric_comp = {}

for r in rubric.keys():
    rubric_comp[r] = make_rubric_components(rubric[r])

print(rubric_comp)

details = rubric_comp
with open('rubrics.py', 'w') as convert_file:
    convert_file.write(json.dumps(details))

print('converted')

