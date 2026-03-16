from django.shortcuts import render


def home(request):
    return render(request, 'heritage_event_centre_app/home.html')


def about(request):
    return render(request, 'heritage_event_centre_app/about.html')


def events(request):

    event_list = [

        {
            "title": "Executive Meeting Room",
            "category": "Conference",
            "image": "heritage_event_centre_app/images/conference.jpg",
            "description": "A professional executive meeting room designed for board meetings, strategy sessions and executive discussions.",
            "date": "May 5, 2026"
        },

        {
            "title": "Corporate Conference Hall",
            "category": "Corporate",
            "image": "heritage_event_centre_app/images/conference_Hall.jpg",
            "description": "A spacious conference hall ideal for seminars, corporate conferences, workshops and training events.",
            "date": "May 10, 2026"
        },

        {
            "title": "Luxury Wedding Reception",
            "category": "Wedding",
            "image": "heritage_event_centre_app/images/event4.jpg",
            "description": "An elegant wedding reception venue designed to create unforgettable wedding celebrations.",
            "date": "May 12, 2026"
        },

        {
            "title": "Banquet Hall Experience",
            "category": "Banquet",
            "image": "heritage_event_centre_app/images/event5.png",
            "description": "A premium banquet setting perfect for gala dinners, celebrations and upscale social gatherings.",
            "date": "May 18, 2026"
        },

        {
            "title": "Royal Wedding Stage",
            "category": "Wedding",
            "image": "heritage_event_centre_app/images/event2.jpg",
            "description": "A beautifully decorated wedding stage designed for engagements, traditional weddings and royal receptions.",
            "date": "May 22, 2026"
        },

        {
            "title": "Grand Celebration Hall",
            "category": "Reception",
            "image": "heritage_event_centre_app/images/event6.jpg",
            "description": "A luxurious and spacious hall perfect for large celebrations, receptions and premium social events.",
            "date": "May 25, 2026"
        }

    ]

    return render(request, 'heritage_event_centre_app/event.html', {"events": event_list})


def contact(request):
    return render(request, 'heritage_event_centre_app/contact.html')