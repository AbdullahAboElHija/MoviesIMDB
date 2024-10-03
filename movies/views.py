from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .forms import ReviewForm

# Create your views here.
from django.http import HttpResponse
from . import forms
def movies_list(request):
    movies = Movie.objects.all().order_by('release_date')
    return render(request,'movies/movies_list.html',{'movies':movies})


def movie_detail(request, slug):
    # Fetch the movie by slug
    movie = get_object_or_404(Movie, slug=slug)
    reviews = movie.reviews.all()  # Get all reviews related to this movie

    if request.method == 'POST':
        if not request.user.is_authenticated:
            # Redirect if user is not authenticated
            return redirect('accounts:login')

        # Handle review form submission
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie  # Set the current movie
            review.user = request.user  # Set the logged-in user
            review.save()
            return redirect('movies:detail', slug=movie.slug)  # Redirect to the same movie detail page
    else:
        review_form = ReviewForm()  # Create an empty form for GET requests

    # Pass the movie, reviews, and form to the template
    return render(request, 'movies/movie_detail.html', {
        'movie': movie,
        'reviews': reviews,
        'review_form': review_form,
    })

@login_required(login_url="/accounts/login/")
def movie_create(request):
    if request.method == "POST":
        form = forms.CreateMovieForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            # Set the author to the logged-in user
            instance.author = request.user  # Automatically assign logged-in user as author
            instance.save()  # Now save the instance with the author
            return redirect('movies:list')
    else:
        form = forms.CreateMovieForm()

    return render(request, "movies/movie_create.html", {"form": form})