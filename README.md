# fight_game

Supuestos:
- Cada personaje tiene un FB distinto
- Cada stat tiene un AS distinto, así como el personaje tiene su propio AS
- La formula del FB retorna un entero entre 0 y 9
- El usuario ingresa el nombre de cada equipo

Decisiones:
- La clase Game es una clase que controla la vida de la simulación, se le otorga un parámetro de tamaño de equipo por si se quisiera cambiar la cantidad de personajes del equipo. En caso de que un equipo tenga la misma cantidad de personajes mismo alignment, el alignment de ese equipo se decidirá en forma aleatoria.
- La clase fightManager es la encargada de llevar a cabo cada batalla de la simulación, haciendose cargo de ver quien parte (de forma aleatoria), de llevar a cabo los ataques, restar las vidas y declarar al ganador
- También esta la clase Team que es la encargada del equipo y de sus miembros, sabe cuantos miembros tiene vivos y quienes
- La clase Character representa a cada personaje del juego, contiene su id, nombre y el conjunto de sus habilidades, además de los otros atributos pedidos se encarga de generar los valores para hp, fb y actualizar los de sus habilidades una vez que tiene el alineamiento del equipo.
- Además utilice una clase llamada powerstat ya que todas las habilidades tienen una forma igual de calcularse recibiendo ciertos parametros base, así que por eso definí una clase para ellos.
- En el archivo service se encuentra todo lo que tiene que ver con el uso de la api superhero, recibe el número de personajes que hay que elegir, hace un fetch a la api para obtener todos los personajes disponibles y después para cada personaje elegido peticiona por su información. Luego, de esta información se retorna solo la que sera ocupada para el juego. La separe por si hubiese que cambiar la api, es más fácil porque la lógica esta encapsulada ahí y no dispersada por el código.
- En el archivo de mailing se encuentra lo necesario para enviar un mail con un template de html. El fightManager y Game tienen variables que almacenan el resumen de la pelea y el resumen del juego, en el se ira escribiendo la presentación de los equipos, el round de pelea y sus jugadores, el ganador del round y finalmente el equipo ganador.
- Se creo un archivo de constantes para manipularlas facilmente
- Además se considero el uso de un .env file para el uso de las apis