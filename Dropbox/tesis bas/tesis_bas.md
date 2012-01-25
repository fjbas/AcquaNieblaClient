Resumen
=======

Los sistemas de adquisición de datos y monitoreo son ampliamente utilizados en el mundo entero como una forma de obtener una mayor eficiencia en la producción y uso de energía. También son ocupados para conocer el estado y la capacidad de funcionamiento en que se encuentra una planta y analizar cómo afecta las distintas modificaciones que se lleven a cabo durante el monitoreo, esto con el objetivo de conocer el aporte real de las modificaciones implementadas.

En la siguiente memoria se expone una estrategia de bajo costo para el desarrollo y la implementación de un sistema de adquisición y monitoreo de datos, además de la descripción de su implementación en un sistema combinado de mediciones climáticas y medidores de eficiencia de recolectores de agua de la neblina. 

En este trabajo abordaremos: las estrategias a utilizar, los objetivos primarios y secundarios del proyecto, junto con las justificaciones de cada una de las decisiones tomadas.
Además describiremos el hardware necesario, la forma de adquisición de los datos y de monitoreo, junto con los modelos matemáticos de cálculo y la descripcion de los programas incluyendo la forma en que éstos funcionan e interactúan con los usuarios. 

INTRODUCCIÓN
============

Motivación
----------

Imaginemos una pequeña planta (eléctrica) donde la temperatura no puede pasar cierta temperatura, razón por la cual éste factor debe ser monitoreado continuamente.
Esto se puede realizar de dos maneras: La primera es mediante la constante  inspección de un termómetro por parte de un funcionario, la segunda es a través de un sistema automático que se encuentre monitoreando el sistema constantemente. El primer método puede resultar costoso e ineficaz debido que dependiendo del tipo de proceso se puede requerir gran tiempo de trabajo de un operario y bastaría un descuido de éste para que las acciones requeridas no sean tomadas a tiempo. El segundo método puede resultar aún mas costoso debido a la necesidad de instalar un sofisticado y complejo sistema automático de monitoreo.

Entonces resalta la necesidad de un sistema de bajo costo, de fácil uso  y configurable a las necesidades de cada uno de sus usuarios capaz de medir en tiempo real el estado de las variables que requieran monitoreo.

Importancia de medir el estado de una planta
--------------------------------------------

La medición de factores a través de sensores  nos pueden entregar gran información acerca del estado actual  de un sistema, permitiéndonos desde simplemente estudiar el comportamiento de éste, hasta mantener el completo control de la planta a través de sistemas retroalimentados. 

El conocer el estado del sistema nos permitirá, desde  comprender algunos fenómenos, mejorar la eficiencia de un sistema de acuerdo a las observaciones hasta  mantener el sistema siempre dentro de rangos preestablecidos a través de la ejecución de acciones mediante actuadores, conocidos como sistemas de control automáticos.

Contexto del problema
---------------------

No es desconocido el hecho que en el desierto existe  escasez de agua, pero lo que no muchos saben es el gran potencial que tiene la Camanchaca -definición de 5 palabras de la camanchaca- en la obtención de agua a través de la extracción de la humedad que se encuentra contenida  en ella.
Hoy en día existe un proyecto que pretende extraer esta humedad y comercializarla permitiendo el desarrollo de las zonas cercanas a éste. 

Pero antes de iniciar la explotación es necesario conocer la real eficiencia de este proyecto, y las opciones de mejoramiento el rendimiento, a través de pruebas realizadas en el lugar donde se instalaran los sistemas. Estos sistemas se encuentran ubicados en zonas  alejadas de los centros de estudio, lo que hace difícil el acceso (acceso a qué), y obliga a construir sistemas que funcione de manera autónoma (y remota?). 
Estos sistemas deberán recolectar  los datos necesarios  y enviarlos a los lugares donde se analizarán. Cabe recordar que los lugares donde se realizará el proyecto presentan una series de dificultades técnicas como son la falta de energía eléctrica, las condiciones climáticas adversas y la falta de un punto de red cercano al lugar donde será instalado el sistema.

Objetivo general  del estudio
------------------------------

El objetivo principal de éste trabajo será diseñar y construir un sistema de adquisición, análisis y envió de datos de bajo costo y de fácil uso para ser instalado tanto en industrias como en hogares y así monitorear diversos factores como temperaturas, humedad, intensidad de la luz o cualquier otro elemento que el usuario desee. El usuario, quien quiera que sea deberá poder adecuarlo a sus necesidades. Además los usuarios podrán acceder de forma remota a la información producida por ésta máquina (qué máquina!). Todos estos elementos compondrán un sistema desde ahora llamado SAED (Sistema de Adquisición y Envió de Datos)

Una vez desarrollada la primera parte de la tesis, se implementara el SAED en una planta de medición climática ubicada en Peñablanca. La instalación del SAED en esta localidad está sujeta a unas series de restricciones que más adelante describiremos.


Objetivos específicos
----------------------

El proyecto se dividirá en dos etapas según las acciones que se requiera:

Etapa 1: Desarrollo del SAED

-	Determinar los equipos necesarios
-	Determinar modo de comunicación
-	Determinar plataforma sobre la que correrán los programas
-	Diseñar software 
-	Determinar limitaciones 
-	Integrar los componentes
-	Realizar simulaciones como si se estuvieran midiendo realmente y analizar los resultados

Etapa 2: Implementación del SAED en el proyecto Acquaniebla 


-	Conocer la locación precisa de laos equipos
-	Determinar las limitaciones existentes
-	Determinar la potencia necesaria para el sistema
-	Elegir el mejor tipo de energía de acuerdo a las condiciones geográficas y proveyendo la mayor seguridad posible al sistema
-	Instalar y testea el funcionamiento del equipo en terreno


Metodología e Hipótesis
-----------------------

Para lograr los objetivos que plantea ésta memoria se dividirá en dos etapas (qué se va a dividir?).

La primera comprenderá el desarrollo de los software y hardware necesario para tener un sistema de adquisición, procesamiento y envió de datos y la segunda comprenderá la implementación de este sistema en un proyecto de monitoreo climatológico  para Acquaniebla  que será implementado en peñablanca  

Al momento de diseñar el proyecto se tendrá en cuenta dos aspectos fundamentales: la robustez del equipo, para evitar todas las posibles fallas y las restricciones presupuestarias.

Para lograr los objetivos mencionados anteriormente será necesarios aplicar conocimientos del área de la ingeniería eléctrica, además será fundamental aplicar técnicas de optimización para reducir costos y llegar a la solución más eficiente posible.

El diseño eléctrico deberá ser simple y robusto con el objetivo de evitar cualquier tipo de falla y que esté dentro de las restricciones presupuestarias, con un bajo costo de instalación y operación. Por éste razón se hará una evaluación económica del proyecto por el periodo propuesto por los clientes y así asegurar que este diseño  cumpla con las restricciones.

Los pasos a seguir son los siguientes:
1.	Revisar literatura acerca de temas relevantes para el desarrollo del sistema
2.	Determinar hardware necesario
3.	Determinar potencia necesarias 
4.	Determinar mejor sistema para proveer energía al sistema
5.	Determinar restricciones del sistema
6.	Determinar los costos y hacer evaluación económica. 
7.	Elegir plataforma Windows, Mac, Linux  
8.	Diseñar los software
9.	Construir el SAED
10.	Probar en laboratorio 
11.	Instalar el proyecto en peñablanca
12.	Testear su funcionamiento.


Estructura de la memoria
------------------------

La estructura de la presente memoria comprende un capitulo de introducción donde:
.
Seguido por un segundo capítulo en el cual:












MARCO TEÓRICO
==============

En este capítulo se explica el funcionamiento de los principales componentes necesarios de los distintos subsistemas que compondrán el sistema de adquisición de datos (SAED). También se indican los procedimientos y tecnologías que podrán ser aplicados para realizar de manera eficiente las distintas tareas. 
     
Los subsistemas que revisaremos serán:
-	Sistema de adquisición de datos SAD
-	Sistemas de potencia de 12V
-	Sistemas de transmisión  de datos
(Como es que un SAD está compuesto por un SAD?)


Sistema de adquisición de datos
-------------------------------

Un SAD es un  conjunto de elementos encargados de recibir la información proveniente de los sensores con el fin de al menos  almacenarla, procesarla, y o presentarla.

Antes de continuar es necesario definir algunos conceptos. 

-	Dato
	
	Representación simbólica (numérica, alfabética...), atributo o característica de un valor. No tiene sentido en sí mismo, pero convenientemente tratado (procesado) se puede utilizar para cálculos o toma de decisiones.

-	Adquisición
	
	Recolección de un conjunto de variables físicas, o eléctricas, que generalmente deben ser digitalizada de manera que se puedan procesar en un computador.

-	Sistema

	Conjunto organizado de dispositivos que interactúan entre sí ofreciendo prestaciones más completas y de más alto nivel

-	Bit de resolución

	Número de bits que el convertidor analógico a digital (ADC) utiliza para representar una señal. Así si se dice que es de resolución de 2 bits solo podremos representar cuatros niveles debido a que: el numero de niveles que se puede representar esta dado por   donde n corresponde al numero de bits a utilizar y en este caso 

-	Rango

	Valores máximo y mínimo entre los que el sensor, instrumento o dispositivo funcionan bajo unas especificaciones.

-	Tasa de muestreo

	Es el numero de muestra que se toman por una unidad de tiempo así si se especifica que tiene una tasa de muestreo de 1kHz significa que tomaran 1000 muestras por segundo.

Sistema de adquisición de datos (SAD)
----------------------------------------

En muchas plantas se pueden recopilar unas series de datos que resultan importante conocer a la hora de estudiar su comportamiento, por lo que resulta de vital importancia captarlo para posteriormente: analizarlos, procesarlos y almacenarlos para poder seguir la evolución del sistema.
Por lo general los datos o variables que se desean captar tienen un carácter analógico mientras que su procesamiento,  almacenamiento y análisis son mucho más eficaces cuando se hace digitalmente. Razón por la cual es necesaria una serie de módulos que permitan pasar las señales desde el mundo analógico al digital. A este conjuntos de módulos se le denomina sistema de adquisición (SAD)


El propósito de la adquisición de datos es medir alguna clase de  fenómeno ya sea físico: como temperatura, humedad, intensidad de luz, etc. o eléctrico como podría ser una voltaje o corriente proveniente de una batería.
La adquisición de datos basada en un computador utiliza una combinación de hardware y software entre los que se encuentran computadores y tarjetas de adquisición. Cada SAD ( sistema de adquisición de datos ) es diferente dependiendo de sus requerimientos de aplicaciones, pero todos comparten una meta en común que es la de adquirir, analizar y presentar información. 
Los sistemas de adquisición de datos incorporan señales, sensores,  acondicionamiento de señales, dispositivos de adquisición de datos y software.






2.1.2) Componentes de un sistema SAD


2.1 imagen sacada de:    

Sensores o transductores: Son los encargados de convertir la variable física a medir
 (temperatura, humedad, presión, etc.) en señal eléctrica. Esta señal eléctrica suele ser de bajos voltajes, con corrientes entre los 4ma y 20ma según el estándar.

Multiplexor: Es el encargado de seleccionar el canal que contiene la señal que va a ser muestreada en cada momento. Si solo se desea utilizar una señal no será necesario utilizar un multiplexor.

Amplificador de instrumentación: es el encargado de amplificar la señal de entrada
 del SAD para que los valores en que oscila la señal de entrada sea lo más parecido al rango en el que funciona el conversor A/D desde ahora ADC, consiguiéndose de esta forma máxima resolución. Así por ejemplo si el rango  de funcionamiento del convertidor es de 0 a 5 volts el amplificador debe ser tal que el máximo valor que tome la señal después de amplificada sea igual a 5V

S&H (Sample & Hold, Muestreo y Retención): Es el encargado de tomar la 
muestra del canal seleccionado (sample) y mantenerla (hold) durante el tiempo que dura la conversión. Este circuito será necesario siempre que la señal de entrada sufra variaciones  durante la conversión.


ADC (Conversor A/D): Es el encargado de realizar la conversión analógico/digital en sí, proporcionando un código digital de salida que representa el valor de la muestra adquirida  en cada momento...  

2.1.3) CARACTERÍSTICAS DE UN SAD


Número de canales: Esta determinado por el número de señales que se desean adquirir  depende del número de señales a adquirir,  por lo que el 	número de canales debe ser igual o superior al número de señales que 	se 	desean adquirir.


Exactitud de la conversión:
La exactitud estará determinada por cada uno de los componentes que intervienen en el proceso de adquisición como son: multiplexores, amplificadores, S/H y ADC, esencialmente. 
Es por esto que el Multiplexor deberá tener una baja resistencia de conducción para no alterar las muestras,  El Amplificador deberá tener una mínima corriente de offset, el tiempo que le tome reaccionar antes variaciones de la señal de entrada tendrá que ser pequeños en comparación con la tasa de muestreo. El  sample and hold: deberá poseer una  Pequeña tensión offset y una gran velocidad de reacción,  manteniéndose constante el tiempo necesario  para que el ADC la digitalice. En general todos los dispositivos desarrollados para el fin de adquirir datos cumplen con estas características por lo que no será necesario preocuparse de ellas.

Pero lo que el usuario debe preocuparse es  la precisión y tasa de muestreo que estarán dada por el ADC, dodo que distintos proyectos requieren distintas combinaciones que deberá tener una resolución acorde a las necesidades, esta estará dado por el número de bits que utilice el ADC, también se requerirá un tiempo de conversión acorde a la tasa de muestreos y además que el muestreo se realice de modo lineal.
Es importante determinar estos dos factores ya que un equipo con mayor precisión y mayor tasa de muestreo, puede significar un mayor costo y obtener más información de la necesaria, por lo que se deberán tener equipos con mayor capacidad de procesamiento y que consume mas recurso.


Velocidad de muestreo (throughput rate): 
Este parámetro especifica la velocidad a la que el SAD puede adquirir y almacenar muestras de las entradas. La velocidad de muestreo se relaciona con el número de muestras por unidad de tiempo que pueden obtenerse.

Así por ejemplo si midiéramos la temperatura de algún elemento que varia cada medio hora, no tendría sentido medir cada milésima de segundo porque obtendríamos una gran cantidad de datos que solo molestarían. Es mas según Teorema de muestreo de Nyquist-Shannon solo es necesario muestrear con una frecuencia el doble a la frecuencia e la señal original, en este caso solo bastaría tomar muestras cada 15 minuto reduciendo considerablemente el numero de muestras tomadas y los datos que se deban almacenar.


Esta velocidad está determinada por: El tiempo de establecimiento del MUX, el tiempo del  establecimiento del amplificador, el tiempo de adquisición del S/H y el Tiempo de conversión del ADC.


2.2.3 imagen obtenida de:



Como es un proceso lineal cada retardo de cada unos de los componentes significa un aumento en la demora en el tiempo de conversión. Por lo que el tiempo de conversión incluye la suma de todos los retardos de las partes antes mencionadas.

Resolución del sistema SAD:
Es la precisión con la que la señal analógica es convertida en señal digital y está dada por la capacidad del ADC específicamente es el mínimo voltaje que puede ser detectado


Por ejemplo si el ADC es de 8 bits   y el rango  de voltaje de la señal de entrada va entre 0 y 5 v se obtendrá que la resolución será de:   o sea cada 0.019 volts que cambie la señal será reflejado en el valor digita


2.1.4) Elementos necesario para la  implementación de un SAD

Sin importan el tipo de SAD que se diseñe, y el uso que se le dé, siempre será necesario contar con los siguientes componentes en todos los SAD que se diseñen, y además se deberá determinar cuáles son los mejores componentes para cada una de las aplicaciones en la que se utilice.

Los elementos básicos son:
Computador o sistema de control y procesamiento de datos
Sensores acorde a lo que se desee medir
Hardware de adquisición
Hardware de análisis, que puede ser propio de la computadora o agregado externamente
 Software  necesario para controlar el proceso y administrar los datos.

2.1.5) Clasificación de los SAD según el tipo de conexión
Los SAD se pueden clasificar según la forma en que adquieran los datos siendo las más típicas:
Las basadas en tarjetas de adquisición de datos (TAD)
Las basadas en interfaces estándar para la instrumentación
Las basadas en circuitos integrados 

Aunque el esquema, independiente del tipo de conexión es el siguiente:

Imagen obtenida de:

Sistemas basados en interfaces internas
Es el sistema SAD mas usado y se implementa conectando tarjetas de adquisición de datos (TAD), directo a los slot de expansión de un computador.  Y los datos pueden ser trabajados directamente, ya que es tratado como una memoria RAM, lo que reduce el tiempo por acceso al hardware. O como un elemento externo que reduce los requerimientos del PC pero aumenta el tiempo de procesamiento.

Sistemas basados en interfaces externas
Son uno o un conjunto de instrumento conectado a través de un BUS de dato, realizando un trabajo determinado controlado por un equipo principal, que habitualmente resulta ser un computador.
Existen distintos estándares para BUS como el IEEE 488, el GPBI o el serial o USB 

A través del BUS se podrá controlar los distintos subsistemas y adema se podrá captar la información proveniente de los ellos, para poder trabajar con ella en el computador

En ambos caso, tanto las TAD, como los dispositivos externos, incluyen muchos de los elementos necesarios antes mencionados para realizar esta tarea de adquisición de datos.



2.1.6) Selección correcta del sistema de adquisición de datos:

A la hora de elegir los componentes se deberán tener en cuentas muchos factores que permita obtener un sistema robusto, que cumpla con los requerimientos y sea del menor costo posible. Esto se traduce en que la elección de los equipos deberá ser rigurosa, procurando no ocupar equipo de menor capacidad debido a que las tareas no van a poder llevarse a cabo, y tampoco sobredimensionar los equipos, ya que se traducirá en un costo innecesario para quien implemente el sistema.

A la hora de seleccionar los equipos se deberá tener en cuenta el uso que se le dará, el sistema de control, tipo y números de señales a medir, hardware necesario.
Además se deberá considerar las ampliaciones presumibles en un corto y mediano plazo, el nivel de integración con equipos nuevos y existentes.

En general el uso que se le va a dar acota el SAD a escoger en distintos aspectos como son: 
Físicos, si deseamos que sea portátil o fijo
Eléctricos, tipo de corriente, voltaje, fuente de alimentación, etc.
Software disponibles
Tipo de profesional que va a ocupar el sistema.

Al momento de seleccionar una TAD o un sistema de adquisición de datos externo deberemos  considerar

Tipo de bus de ordenador para el que está diseñada (XT, AT, EISA, NuBUS, PCI, etc.).
Número de canales analógicos de entrada (modo común y diferencial) y de salida.
Número de canales digitales de entrada y de salida.
Velocidad de muestreo (global o por canal).
Resolución de los DAC/ADC.
Rango dinámico para los ADC.
Ganancia variable para los amplificadores de entrada.
Contadores y temporizadores.
Buses auxiliares para sincronización con otras TAD.
Programación a bajo y/o alto nivel.
Incorporación de DSP (Procesador de señales digitales).
Otros circuitos para aplicaciones específicas (ASIC) que faciliten aspectos de uso y
explotación.
Consumo.
Entorno de programación (Windows, Mac, Linux, etc.).





2.2) Sistemas de potencia de 12V

Todo sistema de potencia esta compuesta por los siguientes subsistemas:
Control principal y monitoreo (CPM)
Tableros
Líneas 
Sistema de almacenamiento
Sistema de generación
Acondicionamiento de corriente continua 
Además de los consumos que son la razón por la cual se construye esto tipo de sistemas. 

2.2.1) Control principal y monitoreo (CPM)

Supervisa la operación global de un sistema de potencia y puede interactuar con las cargas. La principal función de un CPM es asegurar la operación del sistema ya sea en modo automático o manual. 


2.2.2) Tableros 

Es el lugar donde se ubican las protecciones del sistema eléctrico, en general para el caso de 12 volts se ocupan como protección los fusibles.

Fusibles
Los fusibles son elementos de seguridad que interrumpen la energización de un sistema en cuando el consumo de corriente aumenta sobre lo deseado. Evitando el daño de los equipos.

Funcionamiento de los fusibles 
Los fusibles están compuestos por un filamento un elemento conductor que se funde por efecto de la temperatura que se genera al pasar una mayor corriente para la cual fue diseñado.
Mientras mayor sea la corriente que circula, menor será el tiempo que se demore en interrumpir el flujo de corriente, este comportamiento se ve en la siguiente curva tiempo-corriente

Curva de tiempo de ruptura de un fusible según la intensidad de la corriente.








 



2.2.3) Líneas 
Son elementos que conducen la energía a lo larga de todo el sistema desde los punto de generación hasta los consumos, pasando por los sistemas de almacenajes.

En  la líneas debido al paso de la corriente se producen perdidas y caídas de voltajes dadas por:



Caída de voltaje en la línea y perdidas
 Es la diferencia de voltaje que se produce entre el inicio el extremos final de la línea debido a la resistencia que posee el conductor.
 
Y esta dada por 


Donde  corresponde al voltaje al final donde se encuentra el consumo
 Es el voltaje de la fuente 
 Es la intensidad de corriente
 Es la resistencia de la línea dada por

Donde   son la resistividad del conductor, el largo del conductor y la sección del conductor respectivamente. 

Y la pérdida de potencia debido a la resistividad de la línea estará dada por:



Temperatura en las líneas:

Otro factor que también contribuye a modificar la resistencia de una línea es su temperatura. Si la temperatura de los conductores no es de 20° c será necesario modificar la resistencia de la siguiente forma 



Donde es característico para cada uno de los elemento como por ejemplo el del cobre que es de 
Así la resistencia a una temperatura t distinta de 20°c será de:







2.2.3) Fuente de energía

Todo sistema eléctrico de 12 volt al igual que cualquier otro sistema eléctrico requiere obtener su energía de alguna forma. Esta puede ser a través o a una red eléctrica convencional monofásica o trifásica mediante el uso de transformadores y rectificadores de corriente. O través de fuentes propias al sistema de potencia, esta pueden ser del tipo renovable como: eólica,  solar, o hídrica o no renovable como seria a diesel.

Aunque por lo general este tipo de red trabaja separada de la red eléctrica ya que buscan ser autónomas, además suelen ocupar energías renovables y en muy pocas ocasiones se ocupan generadores.  

2.2.4) Sistema de almacenamiento de energía 

Son elementos donde almacenamos la energía producida por los sistemas de generación, para poder ocuparla en el momento que no haya luz. Típicamente son batería 

2.2.5) Acondicionamiento de corriente continúa 
Provee protección a los componentes eléctricos, además convierte la tensión de los sistemas generadores a una tención utilizable  por los equipos 



2.2.6)  Consumos
 Son los elementos del sistema que utilizan la potencia del sistema, por lo que son el punto de partida a la hora de diseñar un sistema potencia, ya que determinaran el tamaño de: las líneas, los fusibles y fuente de energía.

Los consumos pueden ser de distintos tipos  como son:
Motores
Lámparas
Computadores


2.3) Sistemas de transmisión  de datos digitales (incompleto)
Poner típico diagrama de emisor canal, etc.



 

3) Energía solar:

Es la energía producida por el sol en forma de luz. Esta energía es gratuita, prácticamente inagotable, no produce contaminación y esta presente en todo el mundo.
No es difícil entender que todas las energías de la tierra se producen gracias al sol desde la eólica producida por el calentamiento de la superficie terrestre y el aire que produce el flujo de este, pasando por la hidroelectricidad hasta los combustibles fósiles producidos hace miles de años.
Pero la forma de aprovechar esta energía directamente es a través de la absorción de las radiaciones ya sea para producir calor o directamente corriente eléctrica. Que es el caso en el que nos vamos a centrar.
Para comprender la energía solar será necesario tener presente algunos conceptos que son:

Irradiancia
Es la potencia incidente por una unidad de superficie y generalmente se mide en  la irradiancia promedio en la superficie terrestre es de 1000 




Irradiación
Es la integral de la Irradiancia en un intervalo


Azimut 
Es el ángulo o longitud de arco medido sobre el horizonte celeste que forman el punto cardinal sur (Norte) y la proyección vertical del astro sobre el horizonte del observador situado en alguna latitud Norte (Sur). Se mide en grados desde el punto cardinal en sentido de las agujas del reloj: Norte-Este-Sur-Oeste.






3.2) Elementos necesarios para captar la energía solar


Hoy en día con el fin de simplificar las tares y reducir costos se emplean elementos que abarcan mas de un subsistema, y para el desarrollo del sistema  ocuparemos este tipo de elemento

3.2.1) Regulador de carga

Los reguladores de carga cumplen la función de CPM y acondicionador de corriente continua e incluye sistema de protección de sobre corriente.

La función de este elemento es recibir la corriente proveniente de los paneles, regular la tención para que pueda ser utilizada por los consumos y almacenada, además chequea continuamente el nivel de carga de la batería asegurándose de no sobrecargarla ni de descargarla excesivamente para no producir daños en ella. 







3.2.2) Celdas solares
Son elementos de silicio capases de convertir las radiaciones solares en energía eléctrica

Paneles solares
Son un conjunto de células fotovoltaicas, utilizadas para obtener energía eléctrica directamente de la luz solar.
Se pueden clasificar en tres tipos 
Monocristalinas
Policristalinas 
Amorfas 


Sistema de almacenamiento de energía 


Son elementos donde almacenamos la energía por la placa solar, para poder ocuparla en el momento que no haya luz. Típicamente son batería 
Hay de diferente tipo pero para el caso de uso con placas solares tienen que ser del tipo de descarga profunda  ya que soportan mejor las constantes cargas y descargas aumentando su vida útil.






Modo de funcionamiento del sistema de potencia




el panel solar entregar corriente con un voltaje variable entre 0 y 18 volts según la intensidad lumínica sobre esta, potencia que recibirá el regulador de carga el cual la transformara a un voltaje de 12 volts y cargara la batería, y en el caso en que está este completa dejara de enviar energía para no estropearla. Además el mismo regulador proveerá corriente a un voltaje constante a los distintos consumos que tendrá el sistema. 
Normas para un sistema solar

Sección y caída de tención en las líneas

Las secciones de las líneas deberán ser mayores o iguales a entre el generador y el regulador de carga y de entre el regulador y las baterías, además la caída de tención deberá ser menor al 3% entre el generador y el regulador de carga, menor al 1% entre la batería y el regulador y menor al 3% entre el regulador y las cargas




4) ENFOQUE METODOLÓGICO (INCOMPLETO, creo que lo voy a eliminar)

Objetivo principal
Diseñar y construir un sistema capas de adquirir procesar y almacenar los datos provenientes de distintos sensores y debe poder ser usado tanto en mediciones industriales como residenciales. 
Objetivo secundario
Se debe poder acceder a los datos generados de manera remota.
En este caso el tipo de sensores no será importante ya que el sistema por defecto vendrá con ___entradas análogos y ____ digitales o en el caso de necesitar más entradas se podrá aumentar a ____entradas análogas y ____digitales a través. 
Además tampoco será necesario dimensionar la potencia de los sensores debido a que el mayor porcentaje del consumo será producido por el resto del sistema.



Acquaniebla

Es una compañía que pretende
La neblina es de gran interés para os investigadores porque mantiene ecos sistemas y a través de sistema adecuado permite la extracción de agua en lugares donde esta es escasa.  El proyecto de Aqcuaniebla permitirá aumentar la eficiencia de estos sistemas mediantes las mediciones que puedan obtener y contempla el diseño, la construcción y prueba de los sistemas y todos los sensores necesarios 
Sistemas de obtención de potencia
Sistemas de transmisión de datos 

Objetivo general:
Implementar el sistema antes implementado y observar su funcionamiento.






5) LIMITACIONES Y RESTRICCIONES (incompleto)

5.1) Factores a considerar

En el lugar donde será instalado no existe acceso a la red eléctrica por lo que será necesario alimentar el sistema con algún tipo de energía renovable y tampoco hay un punto de red, solo cobertura celular por lo que este deberá ser el medio de transmisión de la información.
Las condiciones climáticas son extremas con temperaturas que van desde los_____ hasta los____ resultando dañinos para equipos que no están diseñados para trabajar bajo estas temperaturas.
Los vientos presentes  arrastran polvo y arena además de la constante humedad presente en la zona, elementos dañinos para los equipos electrónicos, por lo que resulta fundamental contar con un sistema de protección contra estos.

Tipos de sensores que deberán incluirse. 
Pese a no ser relevante que se va a medir, es necesario conocer el tipo de salida del sensor (analógica o digital) el numero de sensores y el consumo de cada uno de ellos para poder dimensionar el sistema de potencia. 


Poner los sensores que deberán ir hacer un resumen del número de entradas y potencia en el diseño. 

6) DISEÑO DEL SISTEMA

En el siguiente capítulo se presentara el diseño del SAD, considerando su funcionamiento, las principales características, los componentes necesarios, y su integración como un todo separándolo en dos etapas, donde la primera etapa corresponde al diseño básico del sistema y la segunda corresponde a la implementación de este sistema en el proyecto Acquaniebla

5.1)  Objetivos General:
Como se menciono anterior mente, el principal objetivo es diseñar y construir un sistema capas de adquirir procesar y almacenar datos de distintos tipos tanto para uso industrial o residencial e implementarlo en una planta de medición.

 5.2) Características del sistema.
El sistema posee las siguientes características, que resultan fundamentales para su funcionamiento, implementación y uso.


Bajo costo: El costo del equipo, instalación y operación debe ser reducido

Robusto: El sistema completo debe ser diseñado y construido de tal manera que el numero de fallas se reduzca al mínimo, con una precisión que más adelante especificaremos según el tipo de medición  y jamás debe quedar inutilizado por lo que debe contar con sistema de reinicio en el caso de que algún error grave ocurra.
Tiempo preciso: el sistema automáticamente tendrá que estar sincronizado con la hora UTC y ajustarse en el caso que ocurra algún desfase.

5.3) Funciones básicas:

Adquisición de información: el sistema deberá ser capaz de adquirir la información de al menos 4 sensores analógico a especificar por el usuario y 6 digitales.

Procesamiento: Una vez que los datos sean recibidos será necesario poder trabajar con ellos según las necesidades del proyecto.

Transmisión  de datos: en algunos casos es posible que en el lugar donde se analizan los datos se encuentren alejados del punto de medición, por lo que será necesario implementar un sistema que permita transmitir esta información. En el caso en que no se cuente con una toma convencional de internet, se podrá expandir el sistema con un kit de comunicación que permitirá transmitir la información pese este impedimento

Suministro de potencia: El diseño del sistema permite trabajar en lugares donde no exista una toma de corriente cercana, por lo que a través de un kit de expansión se podrá trabajar en estas situaciones.



5.4) Diseño principal:
El diseño que se eligió consiste en una tarjeta de desarrollo Olimexino 328  y un computador  común el cual puede funcionar con Ubuntu 11.04 o superior, además de 3 programas como son Python MySql, Sqlite y Dropbox y como programas opcional Microsoft Excel y Matlab  los cuales no son fundamentales, pero puede simplificarle el trabajo a quienes no posean conocimientos en bases de datos:

5.4.1) Hardware básico:
Según lo visto en capitulo anteriores, todo SAD necesita de al menos:

Computador o sistema de control y procesamiento de datos
Sensores acorde a lo que se desee medir
Hardware de adquisición
Hardware de análisis, que puede ser propio de la computadora o agregado externamente
 Software  necesario para controlar el proceso y administrar los datos.


Para la construcción del SAD se eligió una estructura basado en interfaces externas debido a su bajo costo y la posibilidad de expandirse fácilmente al agregar nuevas interfaces.


El hardware que utilizaremos será el siguiente:

Olimexino 328:
Esta tarjeta de desarrollo programable, que presenta en su arquitectura elementos que le permite ser una muy buena interface para un SAD ya que incorpora diferente tipos de BUS como son serial y USB.
Posee 16 canales de entrada o salidas digitales y 6 canales de entrada analógicas.
Pose un acondicionadores de la señales,  multiplexores, reloj propio, Sample And Hold y Convertidor Análogo Digital, no posee un Convertidor Digital Análogo, pero no se requerirá, por lo que no limita el diseño.

La velocidad del muestreo de esta tarjeta es de al menos 15ksps o 15kHz  con una resolución de 10 bit. Además posee un procesador ATMEGA 328 que permite procesar  la señal antes de transmitirla al PC.

Además permite trabajar tanto con Linux o Windows permitiendo una mayor    versatilidad a la hora de elegir los componentes. 
Esta tarjeta está diseñada  para este tipo de trabajo, pose un costo reducido y muy buenas cualidades para este tipo de aplicación como son:
Gran  resistencia a trabajar con distintas temperaturas,  que pueden variar  entre -25° y 85° Celsius.
Está diseñada para trabajar con voltajes de entrada entre  9 y 30 volts.
Tiene un  consumo muy bajo de solo micros amperes.
puede trabajar en tiempo real.
Gran tolerancia al ruido del medio ambiente o producido por los sensores que se le conecte. 
Todas estas son características muy deseables para este tipo de dispositivo.

Computador:
Se podrá ocupar cualquier computador típico existen en cualquier hogar o oficina que tenga menos de dos años y posea Ubuntu 11.04.
La razón de elegir este componente es la reutilización de elementos existentes, lo que reducirá el costo de instalación y contribuye al medio ambiente al no aumentar el uso de nuevo productos, sino de los existentes.
Además los programas a utilizar involucraran un trabajo mínimo para el computado por lo que no se verá afectadas el resto de las funcionalidades del equipo.

Sensores:
Dependiendo del tipo de medición que desee hacer se podrán conectar distintos tipos de sensores, encontrándose una gran gama en el mercado como:
Acelerómetros.
Sensores de corrientes
Sensores de flexión y fuerzas
Sensores de proximidad
Sensores de luz
Sensores de presión, temperatura, humedad.
Sensores de distintos tipos de gases.
Por mencionar algunos, como se puede ver la gama de sensores es amplia por lo que se pueden medir gran cantidad de factores.

Software de control y  procesamiento de datos:
Para el desarrollo del SAED serán necesarios los siguientes programas:
Python, MySql, Sqlite Dropbox, Excel y Matlab siendo los dos ultimo una opción para analizar los datos pero sin ser de carácter obligatorio su uso.

Python:
Es un lenguaje de programación diseñado por Guido van Rossum  pose la característica de ser multi paradigma ya que soporta orientación objeto, programación imperativa y programación funcional. Además es de licencia abierta y multiplataforma, lo que permite, utilizar el mismo programa en diferentes sistemas operativos. Hoy en día es  muy utilizados por toda clase de persona en el mundo lo que permite tener un gran soporte y librerías que facilitan las distintas tareas.
El huso  de este lenguaje permitirá construir programas para el control del sistema, donde se implementara la comunicación entre los dispositivos externos y el computador. Y también para el análisis de datos como ejecutables donde se implementa la comunicación entre los sensores y el computador.

Mysql
Es un sistema de gestión de bases de datos relacional y multiusuario perteneciente a Oracle Corporation. MySql  es un software libre que permite el almacenamiento y huso de los datos de manera  sencilla para el usuario

Sqlite3
Es un sistema de gestión de base de datos autónomo que a diferencia de otras bases de datos trabaja sobre un archivo en el disco y no sobre un servidor, además requiere solo 350 Kb para ser instalada en su totalidad, lo que la hace muy liviana y ocupa muy poco recurso del computador. Además es de licencia libre para ser utilizada tanto en proyectos personales como empresas.



Microsoft Excel
Herramienta de procesamiento de datos a través de hojas de cálculos desarrollado y distribuido por Microsoft,  no es un software libre. su uso se justifica en el caso que los usuarios no tengan experiencia con Python para el procesamiento de los datos.
Si bien no es de carácter gratuito, la mayorías de los usuarios de este sistemas ya poseen una licencia por lo que no debiera significar un costo adicional. 
Su huso es opcional y solo será ocupada para que el usuario pueda trabajar con los datos de manera más simple y  sin tener que usar otros códigos como es el caso de Python.

Matlab (MATrix LABoratory)
Es un software matemático que ofrece un entorno de desarrollo integrado (IDE) con un lenguaje de programación propio, muy útil a la hora de analizar datos de manera eficiente y completa.
El uso de este software será opcional y solo será se deberá usar  cuando a los datos obtenidos se le quieran hacer un análisis más complejo, por el alto costo de la licencia de este se recomienda solo utilizar en casos necesarios y que la investigación lo amerite.

Dropbox
Dropbox es un servicio de alojamiento de archivos multiplataforma en la nube, operado por la compañía Dropbox. El servicio permite a los usuarios almacenar y sincronizar archivos en línea y entre computadoras y compartir archivos y carpetas con otros. Es  gratuito y resulta fundamental a la hora de compartir los datos obtenidos.


5.5) Funcionamiento del sistema

5.5.1) funcionamiento general del sistema 

El dispositivo encargado de recibir los datos de los sensores continuamente estará recibiendo la información de estos, pero solo tomara una muestra cuando el programa principal se lo indique. Este programa continuamente se estará  ejecutándose en el computador, instalado en el lugar de monitoreo. Luego este programa ara las tareas necesitarías descritas en la siguiente sección.
5.5.2) Funcionamiento especifico del sistema

Programa base
El programa principal fue escrito en lenguaje Python por las razones descrita con anterioridad, este programa es el corazón del sistema debido a que  dirige todo el funcionamiento del sistema, llama a otros programas, y se encarga de almacenar la información.


Su funcionamiento se describe en el siguiente diagrama de flujo.



Explicación del diagrama
 El programa primero ve si existen la conexión a la interface computador sensores y crea la conexión en caso de existir en caso contrario se reinicia el programa. Luego se repite el proceso pero ahora con la base de datos instalada en el computador. Estableciendo la conexión en el caso que esté disponible o reiniciando el programa si esta no esta se reiniciara. 
Para almacenar los datos será necesario tener 4 archivos de texto del tipo. TXT los cuales serán modificados de distintas maneras. Estos se crean al inicio del programa en la carpeta donde se encuentre guardado el archivo del programa y  siempre que estos no existan con anterioridad Estos procesos solo se realizaran una sola vez cuando se ejecute por primera vez el programa. Y se consultara la hora UTC para poder tener un registro de la hora en que se realizo las mediciones .

Una vez terminada esta parte se procederá a entrar en un ciclo donde se esperara un segundo, y luego se le enviara una señal a la interface que en ese momento medirá la señal de los sensores y le enviara de vuelta al computador quien la leerá y la utilizara para: guardarla en un archivo “.TXT” junto con la hora, además los guardara en la base de datos y hará el procesamiento deseado con ellos.

La forma de trabajar en los archivo .TXT será la siguiente.
Cada segundo se guardaran los datos en un archivo y al completarse un minuto los archivos de este se traspasaran a otro archivo, borrándose los datos que este contenía. Luego  el segundo archivo almacenara todos los datos hasta que se cumpla una hora, en este momento se copiara este archivo en la carpeta de Dropbox y se traspasara su información a otro archivo que almacenara todas las horas hasta que se cumplan 24 en este momento este archivo es copiado en la carpeta Dropbox con el nombre según describe las especificaciones. Y el tercer archivo será limpiado de datos dejando listo para en pesar almacenar nuevamente todas las horas.
La razón de ocupar esta estructura es que permite subir directamente el archivo a Dropbox cada una hora y al final del día según las especificaciones que del proyecto. 
La estructura del archivo .TXT será la siguiente:


Interface censores computador
Para configurar la interface computador sensores fue necesario programarla en su propio lenguaje, que resulta ser una adaptación de C
El funcionamiento de esta interface se describe en el siguiente diagrama de flujo

 
La interface está continuamente esperando que se establezca la conexión serial, una vez que esta se establece,  queda en espera de recibir información mediante esta vía y al momento de recibir cualquier dato compara con los parámetros internos, y si coincide se realiza muestrea la información de los sensores y posteriormente se envía por medio de este puerto al computador para que el programa principal pueda obtener estos valores.
 







Base de datos 
Para la base de datos se ocupo Mysql y se separo entres tablas que son las siguientes.

La primera tabla corresponde a la de fecha y posee dos recuadros el primero corresponde a un numero que identificara una fecha que estará guardada en el segundo recuadro. El formato del primero recuadro es del tipo____y el del segundo es de_______________
La segunda tabla contiene información de los sensores  en donde el primero corresponde a la etiqueta del sensor el segundo corresponde al tipo del sensor y el tercero es una descripción de este.
El formato del primer recuadro corresponde a ____ y el del segundo y tercero corresponderán a _______
Y por último la tercera tabla será la que contengan las mediciones que se realicen. El primer recuadro tendrá la etiqueta del sensor que se midió, la segunda contendrá la etiqueta de la fecha y hora en que fue medido y por último la tercera contendrá el valor medido para ese sensor.
El formato de los tres recuadros será del tipo_____
Tanto la primera como la tercera tablas se irán actualizando automáticamente a medida que pase el tiempo y se tomen muestras de los sensores.
La utilidad de esta base de datos es que nos permitirá acceder a los datos de manera ordenada 
 


El proceso consiste la replicación automática de la base de datos cada vez que un nuevo dato se agregue lo que permite acceder en tiempo real a la información de los sensores 


Watchdog (perro guardián)
Es un programa que monitoreara constantemente el sistema y en el caso de que se produzca una falla se reiniciara el sistema de manera automática para continuar almacenando información.



5.6) Implementación de este sistema en el proyecto Acquaniebla.
Como segunda parte de la memoria se diseño la implementación  el sistema descrito anterior mente en este proyecto, 

Pero resumiendo Acquaniebla es un proyecto que pretende obtener agua de la neblina a través de atrapas nieblas, hoy en día es una técnica que ya se está realizando pero no existe mucha información acerca del verdadero funcionamiento de estos sistemas, por lo que resulta fundamental la implementación de un sistema de monitoreo que permita obtener los datos en tiempo real o con desfases menores a un día.
Por lo que la implementación del sistema descrito con anterioridad resultara fundamental, para esta tarea, además se tendrá que incluir otros sistemas como serán:
Sistema de potencia:
Es el encargado de proveer la energía necesaria para que todo el sistema funcione correctamente. Y pose los elementos y características descritas en los capítulos anteriores.

5.6.1) Hardware especifico:


Computador FIT-PC2
Es un computador de muy bajo consumo, solo 8 wats capas de correr los programas descritos con anterioridad 
La razón de no ocupar uno computador común es su alto consumo de energía lo que se traduce en un alto costo al construir el sistema de potencia.

Sistema de potencia
El sistema de potencia estará compuesto por un panel solar, una batería, un regulador de carga cables, sistemas de protección.
Los elementos seleccionados son:



Y la razón de su selección se puede ver en el siguiente capítulo donde se calcula la dimensión del sistema.


Sistema de comunicación


5.6.2) Modo de funcionamiento:

El sistema de potencia proveerá la energía necesaria al SAD y los sensores ubicados en distintas partes, a su vez el sistema de datos recuperara la información proveniente de estos y la procesara almacenara y la enviara a otros computadores para tener acceso remoto a estas mediciones.

Calculo de la potencia necesaria y dimensionamiento de los equipos
En la siguiente tabla podremos encontrar la potencia necesaria requerida 

Descripción detallada de cada unos de los componentes



7) Calculo de las dimensiones del sistema y la potencia necesaria 

En el siguiente capítulo se presentara un cálculo de los Costos, las Dimensiones, la Potencia requerida por el diseño y sus  Características

Dimensionamiento de las líneas y sistema de protección

Como ya lo vimos en el capitulo anterior la líneas tienen pedidas y en base a las formulas vista con anterioridad en el capítulo 2 es decir 



Donde   son la resistividad del conductor a 20°C, el largo del conductor y la sección del conductor y la temperatura del cable respectivamente,  es característico para cada uno de los elemento como por ejemplo el del cobre que es de 
Determinaremos la perdidas y al caída de tención por cada uno de los segmentos

Ocuparemos la resistividad el cobre como 

Para poder dimensionar el sistema de potencia resulta fundamental conocer el consumo total del sistema, y la irradiancia disponible en la zona.

Tramos que componen el sistema de potencia
Por razones prácticas dividiremos las líneas del sistema de potencia en tres tramos



El tramo A corresponde a línea entre el panel solar y el regulador de carga.
El tramo B corresponde al tramo comprendido entre la batería y el regulador de carga, es importante notar que el flujo de corriente es en ambas direcciones, por lo que las pérdidas se consideran el doble al momento de calcularlas. 
El tramo C es el comprendido entre el regulador de carga y los consumos. Aunque este tramo en verdad está compuesto por varios tramos comprendido entre el regulado de carga y los sensores, por motivo de simplicidad se hablara como solo uno.

Para poder determinar las perdidas en el tramo C será necesario saber los consumos individuales de cada uno de los componentes, datos entregados en la siguiente tabla.


  


Para determinar las perdidas en las líneas nos basaremos en la normas para este tipo de instalaciones mencionadas en el capítulo de energía solar. Y ocuparemos la máxima potencia que puede utilizarse

Es decir las pérdidas en el tramo C  se dividirán en dos tipos:

1. Computador

Primero dado que el Olimexino y el internet móvil están conectados directamente al computador, se considerara que están en una misma línea.

Se  utilizaran 6 metros de cables de sección de 2,5 y se supondrá una temperatura promedio de 30°C con lo que veremos que la resistencia será de 0,04388736 Ω y dado que circularan 1,35A se tendrá una pérdida de 0,08W y una caída de tención de tan solo un 0,49% que está bajo el 3% reglamentario 

2. Sensores:
El segundo tipo de consumo serán los sensores que no estarán ubicado a mas de 5 metros del regulador y serán 6 sensores distinto, por lo que las perdidas serán de
Utilizando  10 metros de cables de sección de 2,5 y se supondrá una temperatura promedio de 30°C con lo que veremos que la resistencia será de 0,073 Ω y dado que circularan 0,07A  se tendrá una pérdida de 0,00035 y una caída de tención de tan solo un 0,1 % que está bajo el 3% reglamentario y como se consideraron 6 sensores la pérdida total será de 0,0021W

Es decir las pérdidas del tramo C son de  0,082W


Para el cálculo de las perdidas en los tramos A y B ocuparemos el caso en que la corriente que circula sea mayor, para esto recurriremos al capítulo siguiente donde según la radiación solar y los paneles seleccionados obtendremos la corriente total que circula

El largo del tramo A dado por la separación entre los paneles y el regulador nos será superior a 5 metros, por lo que será necesario 10 metros de cable  y ocupando un cable 8  de sección y suponiendo una temperatura promedio de 30°C la resistencia de este será de 0,045716 Ω y como la potencia de las placas elegidas es de 120W la radiación máxima es de 442 W/hr  y el voltaje es en promedio 17V la corriente que circulara será de 3,12 y  la pérdida será de 0,44501783   y la caída de voltaje de solo  un 0,84%


Análogo para el tramo B donde se consideraran 10m de cable de sección 6  y la misma temperatura   obteniendo una resistencia de 0,03047733Ω solo que en este caso las perdidas serán mayores debido a que la tención bajara a 12V incrementando las perdidas a 0,595417375 y con una caída de voltaje de 1,12% 



Dimensionamiento de los paneles solares
Para poder determinarla potencia que requiere los paneles solares fu necesario determinar los consumo de todo el sistema, las perdidas operacionales de los distintos elementos y las perdidas en las líneas, además de la irradiancia de la zona para lo que fue fundamental el estudio de irradiancia “irradiancia solar en el territorio de la república de chile” con el cual se obtuvieron una estimación de la irradiancia en la zona donde se va a colocar los paneles y así poder estimar la energía que se puede generar diariamente.
Según la inclinación y la orientación de un panel se puede obtener mayor o menor cantidad de energía en día, y esta relación cambia según el mes, siendo más efectiva distinta pociones en distintos meces, pero el criterio que se ocupo  fue el mejor caso para el peor mes
Consiste en obtener la energía diaria en los distintos meces y encontrar el mes en el que se produce menos energía, una vez hallado se busca la inclinación y orientación que produzca la mayor cantidad, descartando la posibilidad de ser más eficiente otros meces.

Según el estudio  el peor mes es el de julio en el que en promedio al día solo se reciben 2,653kWH al día en la mejor orientación que corresponde a azimut de 180 grados al norte y una inclinación de 40° con respecto a la tierra.

Existen día en el que la radiación será menor que el promedio y otros en que será mayor que ella por lo que será necesario definir cuantos días podrá funcionar el sistema sin recibir energía del sol, a esto se le llamara factor de Seguridad y principalmente afecta el tamaño de la batería.
Además para poder recuperar la carga de la batería en el caso que haya radiación, los paneles deberán estar sobredimensionados, a este factor lo llamaremos factor de sobredimensión. 
En resumen la irradiancia de la zona, los consumos, y estos dos factores determinaran el tamaño del sistema.


La potencia necesaria será de:


Consideraremos un factor de seguridad de 5 y un de sobredimensión de 35% y una perdida operación de un 20% que incluye las pérdidas de la batería al cargar, del regulador de carga y de los tramos A y B de la líneas.

Podremos concluir que la energía diaria que se requiere es de 196,8 Wh por día y considerando el factor de seguridad de 5 la batería deberá ser de 82 ampere, tamaño que no existe en el mercado por lo que se deberá ocupar una de 100Ahr.
Como la eficiencia de los paneles consultados se encuentra alrededor del 13% veremos que según la irradiancia promedio diría

Donde N= metros cuadrados del panel
Donde resolviendo obtenemos que el necesitamos 0,71  lo que corresponde a un panel de 93W de potencia.

Pero como existe el factor de sobredimensionamiento de 35% los paneles deberán ser de 125W pero lo mas cercano que existe en el mercado son dos de 60W por lo que la potencia será de 120W.









 
Costos:

Anexo 1

Manual de instalación (incompleto y hay que editarlo)

Instalación de los programas necesarios en Linux
Primero se deberá constar con un sistema operativo Ubuntu 11.4 o superior instalado en el computador que se ocupara como servidor.

Primero instalar Mysql a través de ejecutar en la terminal el siguiente comando:
sudo apt-get install Mysql-server  y confirmar la operación, luego poner la clave deseada, pero se recomienda poner como clave "1234" en caso contrario también se deberá cambiar la clave en el archivo Python.

ahora deberemos crear las 3 tablas que vamos a ocupar para almacenar la información en Mysql a través de los códigos:

create table sensores (idsensor integer,type varchar(20),descripcion varchar(100));
e ingresamos información de los sensores a través del siguiente comando donde deberemos modificar los últimos tres elementos dejándolos siempre entre comillas, y se introducirá primero el número del sensor, el nombre de él y por ultimo una descripcion

insert into sensores (idsensor,type,descripcion) values('1','temperatura1','mide la temperatura de la zona 1');
luego deberemos crear la segunda tabla que contendrá la fecha y el ID de la fecha, esto se deberá hacer a través del siguiente código:

create table fecha (idfecha integer,fecha datetime);
y deberemos ingresar un dato de la siguiente manera..
insert into fecha (idfecha,fecha) values('1','20111009230954');


por ultimo tendremos que crear la tercera tabal que contendrá la medición de los sensores, la identidad de la fecha y la id de los sensores

create table medicion (idsensor integer,idfecha integer,valores integer);
y se introducirá un dato de la siguiente manera.
insert into medicion (idsensor ,idfecha, valores) values ('1','1','30');
los datos ingresados en tanto en la segunda como en la tercera tabla no tiene ninguna importancia, solo se ocupan para iniciarla y permitir el correcto funcionamiento del programa.



una vez listo el programa Mysql deberemos instalar la librerías MySQLdb que nos permitirá conectar nuestro programa escrito en Python con la base de datos MySql
para esto escribir en la terminal sudo apt-get install python-mysqldb o sudo apt-get install python-dev
sudo easy_install MySQL-python

Si escribiste mal la tabla escribir lo siguiente para borrarla
Por último deberemos instalar Dropbox para esto hay que bajar de la página de Dropbox http://www.dropbox.com/downloading?src=index el archivo que más se asemeje al sistema operativo que se tiene instalado. Y poner ejecutar con centro de software de Ubuntu y a continuación debes poner en instalar y configurarlo y seguir los pasos indicados
Y configurar la carpeta que compartirá Dropbox con la carpeta donde se almacenaran el programa en Python y así automáticamente se empezara a compartir archivos 

drop table sensosres;
 la segunda tabla contendrá la fecha para lo que aremos:






ahora sincronizaremos esta base de datos con la del servidor de la u.
