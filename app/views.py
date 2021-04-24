from django.shortcuts import render
from .models import report
# Create your views here.
import numpy as np

def index(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        t = request.POST.get('text')

        data = report(name=n,email=e,text=t)
        
        data.save()

    return render(request, 'index.html')




def about(request):
    return render(request, 'about.html')



def rep(request):
    return render(request, 'rep.html',{'objects':report.objects.all()})


def vrc(request):
    arr_1d = []
    arr_2d = []
    if request.method == 'POST':
        x = request.POST.get('stream')
        stream_list = x.split(' ')
        

        for i in stream_list:
            for k in i:
                arr_1d.append(int(k))
            arr_2d.append(arr_1d)
            arr_1d = []

    def vrc(stream):
       


        for i in stream:

            
            number_of_ones = 0

            for j in i:
                if j==1:
                    number_of_ones+=1


            #Check if numbers of ones is odd or even
            if (number_of_ones%2) == 1:
                i.append(1)
            else:
                i.append(0)


        #print(stream)
        return stream
    
    listoflist = vrc(arr_2d)
    context = {'a':listoflist}


    return render(request, 'vrc.html', context)



def lrc(request):
    arr_1d = []
    arr_2d = []
    if request.method == 'POST':
        x = request.POST.get('stream')
        stream_list = x.split(' ')
        

        for i in stream_list:
            for k in i:
                arr_1d.append(int(k))
            arr_2d.append(arr_1d)
            arr_1d = []

    def lrc(stream):
        
        numpy_array = np.array(stream)
        transpose = numpy_array.T
        transpose_list = transpose.tolist()

        for i in transpose_list:
            number_of_ones = 0
            for j in i:
                if j==1:
                    number_of_ones+=1

            #Check if numbers of ones is odd or even
            if (number_of_ones%2) == 1:
                i.append(1)
            else:
                i.append(0)


        numpy_array_2 = np.array(transpose_list)
        transpose2 = numpy_array_2.T
        new_stream_list = transpose2.tolist()

        return new_stream_list

    listoflist = lrc(arr_2d)
    context = {'a':listoflist}
    

    return render(request, 'lrc.html', context)


def vrc_lrc(request):
    arr_1d = []
    arr_2d = []
    if request.method == 'POST':
        x = request.POST.get('stream')
        stream_list = x.split(' ')
        

        for i in stream_list:
            for k in i:
                arr_1d.append(int(k))
            arr_2d.append(arr_1d)
            arr_1d = []


    def vrc_lrc(stream):
        # ---------------------------------------VRC coding

        for i in stream:
            number_of_ones = 0
            for j in i:
                if j==1:
                    number_of_ones+=1


            #Check if numbers of ones is odd or even
            if (number_of_ones%2) == 1:
                i.append(1)
            else:
                i.append(0)

        # ---------------------------------------LRC coding over VRC
        numpy_array = np.array(stream)
        transpose = numpy_array.T
        transpose_list = transpose.tolist()

        for i in transpose_list:
            number_of_ones = 0
            for j in i:
                if j==1:
                    number_of_ones+=1


            #Check if numbers of ones is odd or even
            if (number_of_ones%2) == 1:
                i.append(1)
            else:
                i.append(0)

        numpy_array_2 = np.array(transpose_list)
        transpose2 = numpy_array_2.T
        new_stream_list = transpose2.tolist()

        return new_stream_list
    
    listoflist = vrc_lrc(arr_2d)
    context = {'a':listoflist}
    
    return render(request, 'vrc_lrc.html', context)


def hamming(request):
    Data = ''
    if request.method == 'POST':
        Data = request.POST.get('numdata')

    
    d = len(Data) #number of Original bits
    for r in range(20): #r number of added bits

        if pow(2,r) >= d+r+1:
            break


    r0_list = []
    for h in range(r):
        r0_list.insert(h,"r"+str(h))



    d0_list = [] 
    for h in range(d):
        d0_list.insert(h,"d"+str(h))

    #just copying
    d0 = d0_list.copy()
    r0 = r0_list.copy()



    #Generating Binary Table
    bin_list = []

    for i in range(pow(2,r)):
        bin_list.append(bin(i))
        bin_list[i] = bin_list[i].replace('0b','')

    bin_list.remove('0') # removine first row in table

    data_sequence = []
    # counting number of ones in each row in binary Table
    for a in bin_list:

        num_of_ones = 0
        for i in a:
            if i=='1':
                num_of_ones += 1
        
        
        if len(data_sequence) == (r+d): #to avoid empty list Error
            break
        
        if num_of_ones == 1:
            
            data_sequence.append( r0_list.pop(0) )
            
        else:    
            data_sequence.append( d0_list.pop(0) )


  

    pa_r0 = list()
    pa_r1 = list()
    pa_r2 = list()
    pa_r3 = list()
    pa_r4 = list()
    pa_r5 = list()



    a = 0
    while a < len(data_sequence):
        if data_sequence[a] == "r0": # all increment = 2
            i = data_sequence.index("r0")
            while i < len(data_sequence):
                pa_r0.append( data_sequence[i] )
                i+=2

        if data_sequence[a] == "r1": # all increment = 4
            i = data_sequence.index("r1")
            while i < len(data_sequence):
                if i < len(data_sequence):
                    pa_r1.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r1.append( data_sequence[i] )

                i+=3

        
        if data_sequence[a] == "r2": # all increment = 8
            i = data_sequence.index("r2")
            while i < len(data_sequence):
                if i < len(data_sequence):
                    pa_r2.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r2.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r2.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r2.append( data_sequence[i] )

                i+=5

        
        if data_sequence[a] == "r3": # all increment = 16
            i = data_sequence.index("r3")
            while i < len(data_sequence):
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r3.append( data_sequence[i] )

                i+=9

        if data_sequence[a] == "r4": # all increment = 32
            i = data_sequence.index("r4")
            while i < len(data_sequence):
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r4.append( data_sequence[i] )

                i+=17


        if data_sequence[a] == "r5": # all increment = 64
            i = data_sequence.index("r5")
            while i < len(data_sequence):
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )
                    i+=1
                if i < len(data_sequence):
                    pa_r5.append( data_sequence[i] )

                i+=33



        a+=1

    

    
   
    context = {
        'd':d,
        'r':r,
        'ds':data_sequence,
        'pa_r0':pa_r0,
        'pa_r1':pa_r1,
        'pa_r2':pa_r2,
        'pa_r3':pa_r3,
        'pa_r4':pa_r4,
        'pa_r5':pa_r5,
    }


    return render(request, 'hamming.html', context)


