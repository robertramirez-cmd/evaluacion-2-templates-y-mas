from django.shortcuts import render

def inicio(request):

    contexto = {
        'generos': [
            {
                'id': 'accion', 
                'nombre': 'Acción', 
                'descripcion': 'Películas llenas de adrenalina, combates y explosiones.',
                'peliculas': [
                    {'nombre': 'Mad Max: Fury Road', 'edad': '+14', 'imagen': 'mad_max.jpg'},
                    {'nombre': 'John Wick', 'edad': '+18', 'imagen': 'john_wick.jpg'}
                ]
            },
            {
                'id': 'ciencia_ficcion', 
                'nombre': 'Ciencia Ficción', 
                'descripcion': 'Aventuras futuristas, viajes espaciales y tecnología.',
                'peliculas': [
                    {'nombre': 'Interstellar', 'edad': '+7', 'imagen': 'interstellar.jpg'},
                    {'nombre': 'Blade Runner 2049', 'edad': '+14', 'imagen': 'blade_runner.jpg'}
                ]
            }
        ]
    }
    return render(request, 'inicio.html', contexto)