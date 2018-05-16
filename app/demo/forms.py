from modelqueryform import forms

from demo.models import House

SEARCH_LINKS = {
    '1': {'bed': [4, 5, 6], 'bath': [3, 4], 'garage': [True], 'heat': ['NG', 'Elec', 'Wood']},
    '2': {'bed': [2, 3], 'bath': [1, 2, 3], 'garage': [True, False], 'heat': ['NG', 'Elec']},
    '3': {'bed': [1], 'bath': [1], 'garage': [False], 'heat': ['Elec']}
}


class HouseQueryForm(forms.ModelQueryForm):
    model = House
    include = ['bed', 'bath', 'heat', 'garage']


def process_queryform(request, search=None):
    if request.method == 'POST':
        search_form = HouseQueryForm(request.POST, prefix="house-form")
    else:
        search_form = HouseQueryForm(prefix="house-form")
        if search is not None:
            for key, value in SEARCH_LINKS[search].items():
                search_form.data['house-form-' + key] = value
                search_form.is_bound = True

    return search_form


