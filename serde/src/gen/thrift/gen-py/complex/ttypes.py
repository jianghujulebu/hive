#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class IntString:
  """
  Attributes:
   - myint
   - myString
   - underscore_int
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'myint', None, None, ), # 1
    (2, TType.STRING, 'myString', None, None, ), # 2
    (3, TType.I32, 'underscore_int', None, None, ), # 3
  )

  def __init__(self, myint=None, myString=None, underscore_int=None,):
    self.myint = myint
    self.myString = myString
    self.underscore_int = underscore_int

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.myint = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.myString = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.underscore_int = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('IntString')
    if self.myint is not None:
      oprot.writeFieldBegin('myint', TType.I32, 1)
      oprot.writeI32(self.myint)
      oprot.writeFieldEnd()
    if self.myString is not None:
      oprot.writeFieldBegin('myString', TType.STRING, 2)
      oprot.writeString(self.myString)
      oprot.writeFieldEnd()
    if self.underscore_int is not None:
      oprot.writeFieldBegin('underscore_int', TType.I32, 3)
      oprot.writeI32(self.underscore_int)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Complex:
  """
  Attributes:
   - aint
   - aString
   - lint
   - lString
   - lintString
   - mStringString
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'aint', None, None, ), # 1
    (2, TType.STRING, 'aString', None, None, ), # 2
    (3, TType.LIST, 'lint', (TType.I32,None), None, ), # 3
    (4, TType.LIST, 'lString', (TType.STRING,None), None, ), # 4
    (5, TType.LIST, 'lintString', (TType.STRUCT,(IntString, IntString.thrift_spec)), None, ), # 5
    (6, TType.MAP, 'mStringString', (TType.STRING,None,TType.STRING,None), None, ), # 6
  )

  def __init__(self, aint=None, aString=None, lint=None, lString=None, lintString=None, mStringString=None,):
    self.aint = aint
    self.aString = aString
    self.lint = lint
    self.lString = lString
    self.lintString = lintString
    self.mStringString = mStringString

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.aint = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.aString = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.lint = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI32();
            self.lint.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.lString = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = iprot.readString();
            self.lString.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.lintString = []
          (_etype15, _size12) = iprot.readListBegin()
          for _i16 in xrange(_size12):
            _elem17 = IntString()
            _elem17.read(iprot)
            self.lintString.append(_elem17)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.MAP:
          self.mStringString = {}
          (_ktype19, _vtype20, _size18 ) = iprot.readMapBegin() 
          for _i22 in xrange(_size18):
            _key23 = iprot.readString();
            _val24 = iprot.readString();
            self.mStringString[_key23] = _val24
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Complex')
    if self.aint is not None:
      oprot.writeFieldBegin('aint', TType.I32, 1)
      oprot.writeI32(self.aint)
      oprot.writeFieldEnd()
    if self.aString is not None:
      oprot.writeFieldBegin('aString', TType.STRING, 2)
      oprot.writeString(self.aString)
      oprot.writeFieldEnd()
    if self.lint is not None:
      oprot.writeFieldBegin('lint', TType.LIST, 3)
      oprot.writeListBegin(TType.I32, len(self.lint))
      for iter25 in self.lint:
        oprot.writeI32(iter25)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.lString is not None:
      oprot.writeFieldBegin('lString', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.lString))
      for iter26 in self.lString:
        oprot.writeString(iter26)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.lintString is not None:
      oprot.writeFieldBegin('lintString', TType.LIST, 5)
      oprot.writeListBegin(TType.STRUCT, len(self.lintString))
      for iter27 in self.lintString:
        iter27.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.mStringString is not None:
      oprot.writeFieldBegin('mStringString', TType.MAP, 6)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.mStringString))
      for kiter28,viter29 in self.mStringString.items():
        oprot.writeString(kiter28)
        oprot.writeString(viter29)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)