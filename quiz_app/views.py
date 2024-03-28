from PyMultiDictionary import DICT_WORDNET, MultiDictionary
from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import *
from .models import *


def index(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()

    categories = Category.objects.all()  # get categories from db
    questions = Question.objects.all()
    choices = Choice.objects.all()
    context = {
        'title': ' Home page: Level Up',
        'categories': categories,
        'questions': questions,
        'choices': choices,
        'profile': profile,
    }

    return render(request, 'quiz_app/index.html', context)


def get_questions(request, pk):
    questions = Question.objects.filter(category_id=pk)
    categories = Category.objects.all()
    choices = Choice.objects.all()
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()

    context = {
        'questions': questions,
        'choices': choices,
        'categories': categories,
        'profile': profile,
    }
    return render(request, 'quiz_app/get_questions.html', context)


def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            if user:
                login(request, user)
                messages.success(request, 'You have been successfully logged in')
                return redirect('index')
            else:
                messages.success(request, 'Something went wrong')
                return redirect('login')
        else:
            messages.success(request, 'Something went wrong')
            return redirect('login')
    else:
        login_form = LoginForm
    context = {
        'title': 'Log in',
        'login_form': login_form,
    }
    return render(request, 'quiz_app/login.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, 'You have left your Account')
    return redirect('index')


def register_user(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, 'You have successfully logged in')
            return redirect('login')
        else:
            for field, error in form.errors.items():
                messages.error(request, f'{field}: {error.as_text()}')

    else:
        form = RegisterForm()  # Форма для регистрации

    context = {
        'title': 'Sign in',
        'form': form,
        'profile': profile,
    }

    if not request.user.is_authenticated:
        return render(request, 'quiz_app/register.html', context)
    else:
        return redirect('index')


# Фнукция для страницы профиля
def profile_view(request, pk):
    profile = Profile.objects.get(user_id=pk)
    categories = Category.objects.all()

    context = {
        'title': f'Profile: {request.user.username}',
        'profile': profile,
        'categories': categories,

    }

    return render(request, 'quiz_app/profile.html', context)


# Функция для страницы изменения аккаунта пользователя
def edit_account_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account data has been changed')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')

    else:
        form = EditAccountForm(instance=request.user)

    context = {
        'title': f'Edit Account info: {request.user.username}',
        'form': form,
        'categories': categories,
        'profile': profile,
    }

    return render(request, 'quiz_app/change.html', context)


def edit_profile_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()

    categories = Category.objects.all()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile data has been changed')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')

    else:
        form = EditProfileForm(instance=request.user.profile)

    context = {
        'title': f'Edit Profile info: {request.user.username}',
        'form': form,
        'categories': categories,
        'profile': profile,
    }

    return render(request, 'quiz_app/change.html', context)


def quiz_results(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()
    user = request.user.profile
    categories = Category.objects.all()
    questions = Question.objects.all()

    choices = Choice.objects.filter(
        pk__in=[int(value) for key, value in request.POST.items() if key != 'csrfmiddlewaretoken'])
    correct_answers = choices.filter(is_correct=True).count()

    percent_correct = (correct_answers / len(questions)) * 100 if len(questions) > 0 else 0

    total_questions = len(questions)
    out_of = f'{correct_answers} / {total_questions}'

    user.points = correct_answers
    user.save()

    context = {

        'title': 'Quiz Results',
        'total_questions': total_questions,
        'profile': profile,

        'correct_answers': correct_answers,
        'percent_correct': round(percent_correct, 2),
        'out_of': out_of,

        'categories': categories,

    }
    return render(request, 'quiz_app/results.html', context)


def about_us(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()
    categories = Category.objects.all()  # get categories from db

    context = {
        'title': 'About us',
        'profile': profile,
        'categories': categories,

    }

    return render(request, 'quiz_app/about_us.html', context)


def search_bar(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()
    categories = Category.objects.all()
    context = {

        'profile': profile,
        'categories': categories,

    }

    return render(request, 'quiz_app/search_bar.html', context)


def word(request):
    dictionary = MultiDictionary()

    if request.user.is_authenticated:
        profile = Profile.objects.get(pk=request.user.pk)
    else:
        profile = Profile.objects.all()
    categories = Category.objects.all()
    word = request.GET.get('search')

    try:
        meaning = dictionary.meaning('en', word, dictionary=DICT_WORDNET)

        antonyms = dictionary.antonym('en', word)[:3]
        synonyms = dictionary.synonym('en', word)[:3]

    except Exception as e:

        print(f"There is an error: {e}")

        meaning = None  # Set meaning to None when an error occurs

        antonyms = []

        synonyms = []

        messages.error(request, f"Please make sure that the word '{word}' was written correctly")

    # if 'Verb' in meaning and meaning['Verb']:
    #     meaning_v = meaning['Verb'][:3]
    # else:
    #     meaning_v = ''
    #
    # if 'Adverb' in meaning and meaning['Adverb']:
    #     meaning_adv = meaning['Adverb'][:3]
    # else:
    #     meaning_adv = ''
    #
    # if 'Adjective' in meaning and meaning['Adjective']:
    #     meaning_adj = meaning['Adjective'][:3]
    # else:
    #     meaning_adj = ''
    #
    # if 'Noun' in meaning and meaning['Noun']:
    #     meaning_n = meaning['Noun'][:3]
    # else:
    #     meaning_n = ''

    if meaning is not None:
        if isinstance(meaning, dict):
            meaning_v = meaning.get('Verb', [])[:3]
            meaning_adv = meaning.get('Adverb', [])[:3]
            meaning_adj = meaning.get('Adjective', [])[:3]
            meaning_n = meaning.get('Noun', [])[:3]
        else:
            meaning_v = meaning_adv = meaning_adj = meaning_n = ''
    else:
        meaning_v = meaning_adv = meaning_adj = meaning_n = ''

    context = {
        'profile': profile,
        'categories': categories,

        'word': word,
        'meaning': meaning,
        'meaning_v': meaning_v,
        'meaning_adj': meaning_adj,
        'meaning_adv': meaning_adv,
        'meaning_n': meaning_n,
        'antonyms': antonyms,
        'synonyms': synonyms,
    }
    return render(request, 'quiz_app/word.html', context)
