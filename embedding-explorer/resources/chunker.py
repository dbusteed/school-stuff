chunk_count = 3

def make_chunks(a):
    min_chunk = len(a) // chunk_count
    extra = (len(a) % chunk_count)

    chunks = []

    for i in range(chunk_count):
        if len(chunks) == 0:
            chunks.append( a[:min_chunk] )
        else:
            if extra > 0:
                chunks.append( a[:len(chunks[-1])+min_chunk+1] )
                extra -= 1
            else:
                chunks.append( a[:len(chunks[-1])+min_chunk] )

    print(chunks)

a = [1,2,3,4,5,6,7,8,9,10]
b = [1,2,3,4,5,6,7,8,9]
c = [1,2,3,4,5,6,7,8]
d = [1,2,3,4]

make_chunks(a)
make_chunks(b)
make_chunks(c)
make_chunks(d)