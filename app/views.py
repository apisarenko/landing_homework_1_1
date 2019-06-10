from collections import Counter

from django.shortcuts import render_to_response


counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    if (from_landing == 'original') or (from_landing == 'test'):
        counter_click[from_landing] += 1
    else:
        pass
    return render_to_response('index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')
    counter_show[ab_test_arg] += 1
    if ab_test_arg == 'test':
        return render_to_response('landing_alternate.html')
    else:
        return render_to_response('landing.html')


def stats(request):
    if counter_show['test'] > 0:
        test_conversion = counter_click['test'] / counter_show['test']
    else:
        test_conversion = 0
    if counter_show['original'] > 0:
        original_conversion = counter_click['original'] / counter_show['original']
    else:
        original_conversion = 0
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
