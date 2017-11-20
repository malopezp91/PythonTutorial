# There are five different protocols
import pickle

imelda = ("More Mayhem", "Imelda May", 2011,
          ((1, "Pulling the Rug"),
           (2, "Psycho"),
           (3, "Mayhem"),
           (4, "Kentish Town Waltz")
           ))
even = list(range(2, 10, 2))
odd = list(range(1, 10, 2))

#Protocol zero will create a more readible binary file
with open("protocolZero.pickle", "wb") as protocolZeroFile:
    pickle.dump(imelda, protocolZeroFile, protocol=0)
    pickle.dump(even, protocolZeroFile, protocol=0)
    pickle.dump(odd, protocolZeroFile, protocol=0)

 #Protocol v1 should be readble by earlier versions of python
 #Protocol v2 works on classes and objects more easily, but declared insecured
 #Protocol v3, the default protocol but won't be able to read by Python 2.x     

 #When reading, Python knows which protocol version we used for writing

 #Security: Pickling uses an unsecure protocol
 #You should be unpickling data that you don't trust