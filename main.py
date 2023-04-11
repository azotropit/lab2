з  відкритим ( 'postman.txt' , 'r' ) як  f :
    графік  = []
    для  рядка  в  f :
        row  = [ int ( num ) for  num  in  line . розділити ()]
        графік . додати ( рядок )

# Візьміть непарні вершини зі списку шансів і отримайте всі пари в стовпцях, як показано на попередніх малюнках

def  dijktra ( графік , джерело , ціль ):
    найкоротший  = [ 0  для  i  в  діапазоні ( len ( графік ))]
    вибрано  = [ джерело ]
    l  =  len ( графік )
    # Базовий регістр із джерела
    inf  =  10000000
    min_sel  =  інф
    для  i  в  діапазоні ( l ):
        якщо ( i  ==  джерело ):
            найкоротший [ джерело ] =  0   # графік[джерело][джерело]
        ще :
            якщо ( графік [ джерело ][ i ] ==  0 ):
                найкоротший [ i ] =  інф
            ще :
                найкоротший [ i ] =  графік [ джерело ] [ i ]
                якщо ( найкоротший [ i ] <  min_sel ):
                    min_sel  =  найкоротший [ i ]
                    ind  =  i

    if ( джерело  ==  dest ):
        повернути  0
    # Дійктра в грі
    вибрано . додавати ( інд .)
    while ( ind  !=  dest ):
        # print('ind',ind)
        для  i  в  діапазоні ( l ):
            якщо  я  не  вибраний  : _
                if ( graph [ ind ][ i ] !=  0 ):
                    # Перевірте, чи потрібно оновити відстань
                    if (( graph [ ind ][ i ] +  min_sel ) <  shortest [ i ]):
                        найкоротший [ i ] =  графік [ ind ][ i ] +  min_sel
        temp_min  =  1000000
        # print('shortest:',shortest)
        # print('selected:',selected)

        для  j  в  діапазоні ( l ):
            якщо  j  не  вибрано  : _
                if ( найкоротший [ j ] <  temp_min ):
                    temp_min  =  найкоротший [ j ]
                    ind  =  j
        min_sel  =  temp_min
        вибрано . додавати ( інд .)

    повернення  найкоротший [ призначення ]


# Пошук вершин непарного ступеня в графі

def  get_odd ( графік ):
    градуси  = [ 0  для  i  в  діапазоні ( len ( графік ))]
    для  i  в  діапазоні ( len ( графік )):
        для  j  в  діапазоні ( len ( графік )):
            якщо ( графік [ i ][ j ] !=  0 ):
                ступені [ i ] +=  1

    # друк (градуси)
    шанси  = [ i  для  i  в  діапазоні ( len ( градуси )) , якщо  градуси [ i ] %  2  !=  0 ]
     коефіцієнти повернення

def  gen_pairs ( коефіцієнти ):
    пари  = []
    для  i  в  діапазоні ( len ( коефіцієнти ) -  1 ):
        пари . додати ([])
        для  j  в  діапазоні ( i  +  1 , len ( коефіцієнти )):
            пари [ i ]. додати ([ шанси [ i ], шанси [ j ]])

    print ( 'пари є:' , пари )
    # print('\n')
    повернення  пар

pairs  =  gen_pairs ( get_odd ( графік ))
l  = ( len ( пари ) +  1 ) //  2

сума_пар  = []


def  get_pairs ( pairs , done = [], final = []):
    якщо ( пари [ 0 ][ 0 ][ 0 ] не  виконано  ) :
        зроблено _ додати ( пари [ 0 ][ 0 ][ 0 ])

        для  i  в  парах [ 0 ]:
            f  =  кінцевий [:]
            val  =  зроблено [:]
            if ( i [ 1 ] not  in  val ):
                f . додати ( i )
            ще :
                продовжувати

            якщо ( len ( f ) ==  l ):
                pairings_sum . додавати ( f )
                повернення
            ще :
                val . додати ( i [ 1 ])
                get_pairs ( пари [ 1 :], val , f )

    ще :
        get_pairs ( пари [ 1 :], готово , остаточно )


get_pairs ( пари )
print ( 'pairings_sum' , pairings_sum )

min_sums  = []

для  i  в  pairings_sum :
    s  =  0
    для  j  в  діапазоні ( len ( i )):
        print ( 'i:' , i )
        print ( dijktra ( графік , i [ j ][ 0 ], i [ j ][ 1 ]))
        s  +=  dijktra ( графік , i [ j ][ 0 ], i [ j ][ 1 ])
    мінімальні_суми . додати ( и )

надрукувати ( min_sums )

def  sum_edges ( графік ):
    w_sum  =  0
    l  =  len ( графік )
    для  i  в  діапазоні ( l ):
        для  j  в  діапазоні ( i , l ):
            w_sum  +=  графік [ i ][ j ]
    повернути  w_sum

print ( sum_edges ( graph ))

add_dis  =  min ( min_sums )
print ( add_dis + sum_edges ( graph ))
