import gtool.core.utils.classprocessor as conf
#import gtool.utils.classgen as gen
#import gtool.types.common as t
#from gtool.types.attributes import attribute
#from gtool.namespace import namespace, registerClass
#from gtool.filewalker import filematch, filematchspace, StructureFactory
from gtool.core.utils import projectloader
from gtool.core.utils.output import checkalignment
from gtool.core.plugin import pluginnamespace
import sys


def debug(config):
    print('--- conf debug ---')
    conf.debugClass(config)
    print('--- test ---')


"""
def testCode1(k):
    print('test 1 checks it object magic methods works')
    print('---- testing 1 begins ----')
    x = globals()[k]()
    print(x.__list_slots__)
    x.testprop1 = 'hello'
    print(x.testprop1)
    x.testprop1 = 'world'
    print(x.testprop1)
    x.testprop1 = 'remove this'
    print(x.testprop1)
    x.testprop1 = 'remove'
    print(x.testprop1)
    print("----------")
    x.testprop1 += ['this']
    print(x.testprop1)
    print(x.dynamicproperties())

def testCode2():
    print('test 2 further checks it object magic methods works')
    print('--- test  2 starts ---')
    print('--- number ---')
    x = t.Number()
    y = t.Number()
    y.append(9)
    print(x.listtype)
    print(x)
    x.append(1)
    x += y
    print(x)
    print(type(x))
    z = t.Number()
    print(type(z))
    z.append(3)
    z.append(4)
    c = z + x
    print(c)
    print(type(c))
    print('--- string ---')
    h = t.String()
    print(h.listtype)
    print(h)
    h.append('1')
    try:
        # this should file
        h += ['str', 'str2']
    except Exception as err:
        print(err)
    i = t.String()
    i.append('2')
    i.extend(['3','4'])
    h += i
    print(h)
    print('--- test ends ---')

def testcode4():
    print('test 4 checks it basic object creation works')
    x = t.Number([1,2,3])
    print(len(x))
    y = t.Number()
    print(y)

def test3():
    def testCode(k):
        print('test 3 is an earlier alternative of test 6')
        print('---- testing 3 begins ----')
        print('--- test prop 1 ---')
        dClass = namespace()[k]
        x = dClass(
            testprop1=['test0', 'test1'],
            testprop2=t.Number([9], singleton=True, min=0, max=9)
        )
        # property already exists
        x.testprop1.append('test2')
        try:
            # this should file
            x.testprop1.append(1)
        except Exception as err:
            print(err)
        x.testprop1.append('test3')
        x.testprop1.append('test4')
        print(x.testprop1)
        print('--- test prop 2 ---')
        print(x.testprop2.issingleton())
        print(x.testprop2)
        try:
            x.testprop2.append(2)
        except Exception as err:
            print(err)
        print(x.testprop2)
        print('--- test prop 4 ---')
        print(x.testprop4)
        try:
            x.testprop4.append(9)
        except ValueError:
            print("tried to add a value greater than %s" % x.testprop4.max)
        x.testprop4.append(7)
        print(x.testprop4)

        print(x)
        print('--- test 3 ends ---')

    f = open('test\\test3.txt', 'r')
    testString = f.read()
    config = conf.readClass(testString)
    # debug(config)
    classDict = conf.processClass(config)
    for k, v in classDict.items():
        gen.generateClass(k, v)
        testCode(k)

def testCode5(k):
    print('test 5 will check if data loading works correctly')
    print('---- testing 5 begins ----')
    testFile = 'test\\testdata5.txt'

    dClass = namespace()[k]
    x = dClass()
    print('--- test data loaded ---')
    x.load(testFile)
    print(x)
    print('--- test 5 ends ---')

def test5():
    f = open('test\\test5.txt', 'r')
    testString = f.read()
    config = conf.readClass(testString)
    # debug(config)
    classDict = conf.processClass(config)
    for k, v in classDict.items():
        gen.generateClass(k, v)
        testCode5(k)

# use tests 6+

def test6():
    def testCode(k):
        print(
            'test 6 will determine if validation works properly and also includes first introduction of metas in conf')
        print('---- testing 6 begins ----')
        print('--- test prop 1 ---')
        dClass = namespace()[k]
        x = dClass(
            testprop2=t.Number([8], singleton=True, max=8),
            testprop1=['test0', 'test1']
        )
        print('maxlength:', x.testprop1.maxlength)
        # property already exists
        x.testprop1.append('test2')
        try:
            # this should fail
            x.testprop1.append(1)
        except Exception as err:
            print(err)
        x.testprop1.append('test3')
        try:
            x.testprop1.append('test4aa')
        except ValueError:
            print('attempted to add a value that was longer than permitted')
        print(x.testprop1)
        print('--- test prop 2 ---')
        try:
            x.testprop2.append(2)
        except Exception as err:
            print(err)
        print(x.testprop2)
        print('--- test 6 ends ---')

    f = open('test\\test6.txt', 'r')
    testString = f.read()
    config = conf.readClass(testString)
    # debug(config)
    classDict = conf.processClass(config)
    for k, v in classDict.items():
        gen.generateClass(k, v)
        testCode(k)

def test7():

    def testCode7(k):
        dClass = namespace()[k]
        x = dClass(
            testprop1=[1, 2, 3, 4]
        )
        print(x.metas)
        print(x.classfile)
        print(filematchspace())

    print('test 7 verifies metas in conf')
    print('---- testing 7 begins ----')
    f = open('test\\test7.txt', 'r')
    testString = f.read()
    config = conf.readClass(testString)
    # debug(config)
    classDict = conf.processClass(config)
    for k, v in classDict.items():
        gen.generateClass(k, v)
        #registerClass(k, classObject)
        # testCode7(k)
    #print('given \'criteria\' I match for:', filematch('criteria'))
    #print('given \'cr1\' I match for:', filematch('cr1'))

    #print('namespace:', namespace())
    print('--- walk file system ---')
    mypath = 'test\\test7data'
    from os import listdir
    from os.path import isfile, join
    print('filematch space:', filematchspace())
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for filename in onlyfiles:
        print('\n*** file: ', filename, ' processing start ***')
        fname = filename.split('.')[0]
        #print('inside for loop:', namespace())
        _class = filematch(fname)
        if _class is not None:
            d = _class()
            d.load(mypath + '\\' + filename)
            print(d)
    print('--- test 7 ends ---')

def test8():
    def testCode8(k):
        print(
            'test 8 will determine if the new format of multiple (non-singletons) attribs as members of a list works')
        print('---- testing 8 begins ----')
        print('--- test prop 1 ---')
        dClass = namespace()[k]
        x = dClass(
            testprop2=t.Number([8], singleton=True, max=8),
        )
        print(x.testprop2)
        print('--- test 8 ends ---')

    f = open('test\\test8.txt', 'r')
    testString = f.read()
    config = conf.readClass(testString)
    # debug(config)
    classDict = conf.processClass(config)
    for k, v in classDict.items():
        gen.generateClass(k, v)
        testCode8(k)

def test9():
    print('test 9 checks if basic type creation works with the new attribute structure')
    x = t.Number(9)
    y = t.Number(4)
    print(x)
    print('attribute object test')
    a = attribute(typeclass=t.Number,
                  singleton=True,
                  parent='Parent1',
                  attributename='testprop1',
                  kwargs={'max':8}
                  )
    try:
        a.__load__(x) # should raise an Error
    except Exception as err:
        print(err)
    try:
        a.__load__([y,y]) # should raise an Error
    except Exception as err:
        print(err)
    a.__load__(y) # should work

    print(a)
    b = attribute(typeclass=t.Number,
                  singleton=False,
                  parent='Parent1',
                  attributename='testprop1',
                  kwargs={'max':10}
                  )
    b.__load__([x,y]) # should work
    print(b)

def test10():
    def testCode(k):
        print(
            'test 10 will determine if validation works properly as well as classgen with new attribute structure')
        print('---- testing 10 begins ----')
        print('should work...')
        dClass = namespace()[k]
        x = dClass(
            testprop1=t.Number(9),
            testprop2=[t.Number(8),t.Number(1)],
        )
        print(x)

        print('\nshould throw an error...')
        try:
            y = dClass(
                testprop1=t.Number(11),
                testprop2=[t.Number(8), t.Number(1)],
            )
            print(y)
        except Exception as err:
            print('...it did')
            print('got the following error message:', err)
        print('--- test 10 ends ---')

    f = open('test\\test10.txt', 'r')
    testString = f.read()
    config = conf.readClass(testString)
    # debug(config)
    classDict = conf.processClass(config)
    for k, v in classDict.items():
        gen.generateClass(k, v)
        testCode(k)

def test11():

    print('test 11 loads data that contains multiples in the property field')
    print('---- testing 11 begins ----')
    f = open('test\\test11.txt', 'r')
    testString = f.read()
    config = conf.readClass(testString)
    # debug(config)
    classDict = conf.processClass(config)
    for k, v in classDict.items():
        gen.generateClass(k, v)
        #registerClass(k, classObject)
        # testCode7(k)
    #print('given \'criteria\' I match for:', filematch('criteria'))
    #print('given \'cr1\' I match for:', filematch('cr1'))

    #print('namespace:', namespace())
    print('--- walk file system ---')
    mypath = 'test\\test11data'
    from os import listdir
    from os.path import isfile, join
    print('filematch space:', filematchspace())
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for filename in onlyfiles:
        print('\n*** file: ', filename, ' processing start ***')
        fname = filename.split('.')[0]
        #print('inside for loop:', namespace())
        _class = filematch(fname)
        if _class is not None:
            d = _class()
            d.load(mypath + '\\' + filename)
            print(d)
    print('--- test 11 ends ---')

def test12():

    print('test 12 validates auto loading from simple files, multi item data loads and new required arg')
    print('---- testing 12 begins ----')
    __loadclasses('test\\test12.txt', dbg=False)

    print('--- walk file system ---')
    mypath = 'test\\test12data'
    sf3 = StructureFactory.treewalk(mypath)

    print('--- explore results ---')
    for child in sf3.children:
        print(child.dataasobject)

    print('--- test 12 ends ---')

def test13():

    print('test 13 validates auto loading from complex folder structures')
    print('---- testing 13 begins ----')
    __loadclasses('test\\test13.txt', dbg=False)

    print('--- walk file system ---')
    mypath = 'test\\test13data'
    sf3 = StructureFactory.treewalk(mypath)

    print('--- explore results ---')
    for child in sf3.children:
        print(child.dataasobject)

    print('--- test 13 ends ---')

def test14():

    print('test 14 validates chained config and chained data reading')
    print('---- testing 14 begins ----')
    __loadclasses('test\\test14.txt', dbg=False)

    print('--- walk file system ---')
    mypath = 'test\\test14data'
    sf = StructureFactory.treewalk(mypath)

    print('--- explore results ---')
    for child in sf.children:
        print(child.dataasobject)

    print('--- test 14 ends ---')
"""

#--- old tests pre 15 won't work without refactoring to use new project structure

def test15():

    print('test 15 validates loading multiple class files from a predefined directory and the new plugin loader')
    print('---- testing 15 begins ----')
    sf = projectloader('test\\test15', dbg=False)

    print('--- explore results ---')
    for child in sf.children:
        print('-----')
        print(child.dataasobject)

    print('--- test 15 ends ---')

def test16():

    print('test 16 common type plugins')
    print('---- testing 16 begins ----')
    sf = projectloader('test\\test16', dbg=False)

    print('--- explore results ---')
    for child in sf.children:
        print('-----')
        print(child.dataasobject)

    print('--- test 16 ends ---')

def test17():
    outputscheme = '1' #TODO fix test17 config file's output scheme
    print('test 17 validates output format strings and config works')
    print('---- testing 17 begins ----')

    sf = projectloader('test\\test17', dbg=False)

    print('--- explore results ---')
    for child in sf.children:
        #print(child)

        _x = child.dataasobject
        print(_x.output(outputscheme=outputscheme))

    print('--- test 17 ends ---')

def test18sub1():
    print('test 18sub1 validates the matrix class works')
    print('---- testing 18sub1 begins ----')
    from gtool.core.types.matrix import Matrix

    m = Matrix(startwidth=10, startheight=2)

    for x in m:
        print(x)

    print(m.__v_utilization__())

    print(m.__h_utilization__())

    print(m.cursor)

    m.insert(cursor=(2, 1), datalist=['x'] * 20)

    for x in m:
        print('len:', len(x), '-->', x)

    m.bulk_insert(cursor=(2, 2), rows=[['y'] * 10] * 3)

    m.trim()

    print('m v util:',m.__v_utilization__())

    print('m h util:',m.__h_utilization__())

    print('m cursor:',m.cursor)

    for x in m:
        print('len:', len(x), '-->', x)

    print('column 3:', m.col(3))
    mmap = m.__matrixmap__()
    print('*' * 20)
    for x in mmap:
        print(x)

    print('mmap v util:', mmap.__v_utilization__())

    print('mmap h util:', mmap.__h_utilization__())

    print('mmap cursor:',mmap.cursor)

    for x in mmap:
        print('len:', len(x), '-->', x)
    print('--- test 18sub1 ends ---')


def test18():

    outputscheme = '1' #TODO fix test18 config file's output scheme
    print('test 18 validates arbitrarily structured data folder structures work properly')
    print('---- testing 18 begins ----')

    sf = projectloader('test\\test18', dbg=False, outputscheme=outputscheme)

    #print(sf.treestructure())

    s = set()

    """for i in sorted(flatten(sf.treestructure())):
        #print(i)
        s.add(i)

    print(s)
    """

    print('--- explore results ---')
    for child in sf.children:
        print(child)

        print(child.treestructure())
        #_x = child.dataasobject
        #print(_x.output(outputscheme=outputscheme))

    print('--- test 18 ends ---')

    """
    # expected output
    --- explore results ---
    dk1
    objectsInDirectories: False
    objectsInFiles: False
    {'SUBA': ['TESTCLASSSFOURTEEN']}
    dk2
    SUBA
    dk3
    objectsInDirectories: False
    objectsInFiles: False
    {'SUBA': ['TESTCLASSSFOURTEEN']}
    dk4
    objectsInDirectories: False
    objectsInFiles: False
    objectsInDirectories: False
    objectsInFiles: True
    {'SUBA': ['TESTCLASSSFOURTEEN', 'TESTCLASSSFOURTEEN']}
    dk5
    objectsInDirectories: False
    objectsInFiles: False
    objectsInDirectories: True
    objectsInFiles: False
    {'SUBA': ['TESTCLASSSFOURTEEN', 'TESTCLASSSFOURTEEN']}
    dk6
    objectsInDirectories: False
    objectsInFiles: False
    {'SUBA': ['TESTCLASSSFOURTEEN']}
    --- test 18 ends ---

    """


def test19():

    outputscheme = '1'
    print('test 19 validates data alignment works')
    print('---- testing 19 begins ----')

    sf = projectloader('test\\test19', dbg=False, outputscheme=outputscheme)

    try:
        checkalignment(sf)
    except ValueError as err:
        print(err)
        sys.exit(1)

    print('--- explore results ---')
    for child in sf.children:
        print(child)

        #print(child.treestructure())
        _x = child.dataasobject
        print(_x)

    print('--- test 19 ends ---')


def test20():

    outputscheme = '1'
    print('test 20 validates data alignment works')
    print('---- testing 20 begins ----')

    sf = projectloader('test\\test20', dbg=False, outputscheme=outputscheme)

    """
    try:
        checkalignment(sf)
    except ValueError as err:
        print(err)
        sys.exit(1)
    """

    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    _ret.trim()

    for row in _ret:
        print(row)

    #Correct output
    """
    ['dk (d1 ipsum lorum horus) dn', 'dk1 test 123\nhello world', 'defaulttdk1 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0']
    ['dk (d2 ipsum lorum horus) dn', 'test 123', '']
    ['dk (d3 ipsum lorum horus) dn', 'test 123\nhello world', 'defaulttdk3-1 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0']
    ['dk (d4 ipsum lorum horus) dn', 'test 123\nhello world', 'defaulttdk4-1 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0']
    [None, None, 'defaulttdk4-2 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0']
    ['dk (d5 ipsum lorum horus) dn', 'test 123\nhello world', 'defaulttdk5-1 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0']
    [None, None, 'defaulttdk5-2 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0']
    ['dk (d6 ipsum lorum horus) dn', 'test 123\nhello world', 'defaulttdk6 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0']
    """

    """
    for child in sf.children:
        #print(child)

        #print(child.treestructure())
        _x = child.dataasobject
        #print(_x)
        _x.output()
        #print(_x.output()
    """

    print('--- test 20 ends ---')

def test21():
    outputscheme = '1'
    print('test 21 validates data alignment works with trailing non-dynamic attributes')
    print('---- testing 21 begins ----')

    sf = projectloader('test\\test21', dbg=False, outputscheme=outputscheme)

    """
    try:
        checkalignment(sf)
    except ValueError as err:
        print(err)
        sys.exit(1)
    """

    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    _ret.trim()

    for row in _ret:
        print(row)

    # correct output
    """
    ['dk (d1 ipsum lorum horus) dn', 'defaulttdk1 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0', 'dk1 test 123\nhello world']
    ['dk (d2 ipsum lorum horus) dn', '', 'test 123']
    ['dk (d3 ipsum lorum horus) dn', 'defaulttdk3 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0', 'test 123\nhello world']
    ['dk (d4 ipsum lorum horus) dn', 'defaulttdk4-1 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0', 'test 123\nhello world']
    [None, 'defaulttdk4-2 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0', None]
    ['dk (d5 ipsum lorum horus) dn', 'defaulttdk5-1 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0', 'test 123\nhello world']
    [None, 'defaulttdk5-2 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0', None]
    ['dk (d6 ipsum lorum horus) dn', 'defaulttdk6 ipsum lorum horus\nalpha beta\nipsum lorum horus rictum\n4.0', 'test 123\nhello world']
    """

    print('--- test 21 ends ---')

def test22():
    outputscheme = '1'
    print('test 22 validates data alignment of non-concatted dynamic with trailing non-dynamic attributes')
    print('---- testing 22 begins ----')

    sf = projectloader('test\\test22', dbg=False, outputscheme=outputscheme)

    """
    try:
        checkalignment(sf)
    except ValueError as err:
        print(err)
        sys.exit(1)
    """

    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    _ret.trim()

    for row in _ret:
        print(row)

    # correct output
    """
    ['testpropd1', 'testprop1', 'testprop2', 'testprop3', 'testpropd2']
    ['d1 ipsum lorum horus', 'tdk1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', 'dk1 test 123\nhello world']
    ['d2 ipsum lorum horus', '', '', '', 'test 123']
    ['d3 ipsum lorum horus', 'tdk3 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', 'test 123\nhello world']
    ['d4 ipsum lorum horus', 'tdk4-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', 'test 123\nhello world']
    [None, 'tdk4-2 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', None]
    ['d5 ipsum lorum horus', 'tdk5-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', 'test 123\nhello world']
    [None, 'tdk5-2 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', None]
    ['d6 ipsum lorum horus', 'tdk6 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', 'test 123\nhello world']
    """

    print('--- test 22 ends ---')

def test23():
    outputscheme = '1'
    print('test 23 validates data alignment of trailing non-concatted dynamic attributes')
    print('---- testing 23 begins ----')

    sf = projectloader('test\\test23', dbg=False, outputscheme=outputscheme)

    """
    try:
        checkalignment(sf)
    except ValueError as err:
        print(err)
        sys.exit(1)
    """
    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    _ret.trim()

    for row in _ret:
        print(row)

    # correct output
    """
    ['testpropd1', 'testpropd2', 'testprop1', 'testprop2', 'testprop3']
    ['d1 ipsum lorum horus', 'dk1 test 123\nhello world', 'tdk1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d2 ipsum lorum horus', 'test 123', '', '', '']
    ['d3 ipsum lorum horus', 'test 123\nhello world', 'tdk3-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d4 ipsum lorum horus', 'test 123\nhello world', 'tdk4-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    [None, None, 'tdk4-2 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d5 ipsum lorum horus', 'test 123\nhello world', 'tdk5-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    [None, None, 'tdk5-2 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d6 ipsum lorum horus', 'test 123\nhello world', 'tdk6 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    """

    print('--- test 23 ends ---')

def test24():
    outputscheme = '1'
    print('test 24 validates data alignment of trailing non-concatted dynamic attributes')
    print('---- testing 24 begins ----')

    sf = projectloader('test\\test24', dbg=False, outputscheme=outputscheme)

    """
    try:
        checkalignment(sf)
    except ValueError as err:
        print(err)
        sys.exit(1)
    """
    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    _ret.trim()

    for row in _ret:
        print(row)

    # correct output
    """
    ['testpropd1', 'testpropd2', 'testprop1', 'testprop2', 'testprop3']
    ['d1 ipsum lorum horus', 'dk1 test 123\nhello world', 'tdk1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d2 ipsum lorum horus', 'test 123', '', '', '']
    ['d3 ipsum lorum horus', 'test 123\nhello world', 'tdk3-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d4 ipsum lorum horus', 'test 123\nhello world', 'tdk4-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    [None, None, 'tdk4-2 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d5 ipsum lorum horus', 'test 123\nhello world', 'tdk5-1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    [None, None, 'tdk5-2 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d6 ipsum lorum horus', 'test 123\nhello world', 'tdk6 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    """

    print('--- test 24 ends ---')

def test25():
    outputscheme = '1'
    print('test 25 validates direct recursion check works')
    print('---- testing 25 begins ----')

    sf = projectloader('test\\test25', dbg=False, outputscheme=outputscheme)

    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    # correct output
    """
    A recursive loop has been detected in */CLASSONE/CLASSONE.
    The class CLASSONE is seen twice in the same path.
    Make sure that one class does not call itself, either directly or indirectly.
    """

    print('--- test 25 ends ---')

def test26():
    outputscheme = '1'
    print('test 26 validates indirect recursion check works')
    print('---- testing 26 begins ----')

    sf = projectloader('test\\test26', dbg=False, outputscheme=outputscheme)

    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    # correct output
    """
    A recursive loop has been detected in */CLASSONE/CLASSTWO/CLASSONE.
    The class CLASSONE is seen twice in the same path.
    Make sure that one class does not call itself, either directly or indirectly.
    """

    print('--- test 26 ends ---')

def test27():
    outputscheme = '1'
    print('test 27 checks simple output to excel')
    print('---- testing 27 begins ----')

    sf = projectloader('test\\test27', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['EXCEL']()

    _ret = o.output(sf, output='..\\test27.xlsx')

    print(_ret)
    # correct output
    """
    True
    """

    print('--- test 27 ends ---')

def test28():
    outputscheme = '1'
    print('test 28 checks split output to excel')
    print('---- testing 28 begins ----')

    sf = projectloader('test\\test28', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['EXCEL']()

    _ret = o.output(sf, output='..\\test28.xlsx')

    print(_ret)
    # correct output
    """
    True
    """

    print('--- test 28 ends ---')

def test29a():
    outputscheme = 'json'
    print('test 29a tests json output to screen')
    print('---- testing 29a begins ----')

    sf = projectloader('test\\test29', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['JSON']() #TODO read engine from config

    _ret = o.output(sf)

    print(_ret)
    # correct output
    """
    [
        {
            "suba1": {
                "testpropa1": [
                    "d1 ipsum lorum horus"
                ],
                "testpropa2": [
                    "hello world"
                ],
                "testpropa3": [
                    {
                        "testpropb1": [
                            "subc1 ipsum lorum horus"
                        ],
                        "testpropb2": [
                            "alpha beta",
                            "ipsum lorum horus rictum"
                        ],
                        "testpropb3": [
                            4.0
                        ]
                    }
                ],
                "testpropa4": [
                    {
                        "testpropc1": [
                            "subb1 ipsum lorum horus"
                        ],
                        "testpropc2": [
                            "alpha beta",
                            "ipsum lorum horus rictum"
                        ],
                        "testpropc3": [
                            4.0
                        ]
                    }
                ]
            }
        },
        {
            "suba2": {
                "testpropa1": [
                    "d1 ipsum lorum horus"
                ],
                "testpropa2": [
                    "hello world"
                ],
                "testpropa3": [
                    {
                        "testpropb1": [
                            "subc1 ipsum lorum horus"
                        ],
                        "testpropb2": [
                            "alpha beta",
                            "ipsum lorum horus rictum"
                        ],
                        "testpropb3": [
                            4.0
                        ]
                    }
                ],
                "testpropa4": [
                    {
                        "testpropc1": [
                            "subb1 ipsum lorum horus"
                        ],
                        "testpropc2": [
                            "alpha beta",
                            "ipsum lorum horus rictum"
                        ],
                        "testpropc3": [
                            4.0
                        ]
                    }
                ]
            }
        }
    ]
    """

    print('--- test 29a ends ---')

def test29b():
    outputscheme = 'json'
    print('test 29b tests json output to file')
    print('---- testing 29b begins ----')

    sf = projectloader('test\\test29', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['JSON']() #TODO read engine from config

    _ret = o.output(sf, output='..\\test29b.json')

    print(_ret)
    # correct output
    """
    True
    """

    print('--- test 29b ends ---')

def test29c():
    outputscheme = 'yaml'
    print('test 29c tests yaml output to screen')
    print('---- testing 29c begins ----')

    sf = projectloader('test\\test29', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['YAML']() #TODO read engine from config

    _ret = o.output(sf)

    print(_ret)
    # correct output
    """
    -   suba1:
        testpropa1: [d1 ipsum lorum horus]
        testpropa2: [hello world]
        testpropa3:
        -   testpropb1: [subc1 ipsum lorum horus]
            testpropb2: [alpha beta, ipsum lorum horus rictum]
            testpropb3: [4.0]
        testpropa4:
        -   testpropc1: [subb1 ipsum lorum horus]
            testpropc2: [alpha beta, ipsum lorum horus rictum]
            testpropc3: [4.0]
    -   suba2:
            testpropa1: [d1 ipsum lorum horus]
            testpropa2: [hello world]
            testpropa3:
            -   testpropb1: [subc1 ipsum lorum horus]
                testpropb2: [alpha beta, ipsum lorum horus rictum]
                testpropb3: [4.0]
            testpropa4:
            -   testpropc1: [subb1 ipsum lorum horus]
                testpropc2: [alpha beta, ipsum lorum horus rictum]
                testpropc3: [4.0]
    """

    print('--- test 29c ends ---')

def test29d():
    outputscheme = 'yaml'
    print('test 29d tests yaml output to file')
    print('---- testing 29d begins ----')

    sf = projectloader('test\\test29', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['YAML']() #TODO read engine from config

    _ret = o.output(sf, output='..\\test29d.yaml')

    print(_ret)
    # correct output
    """
    True
    """

    print('--- test 29d ends ---')

def test30():
    outputscheme = '1'
    print('test 30 checks simple output to csv')
    print('---- testing 30 begins ----')

    sf = projectloader('test\\test30', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['CSV']()

    _ret = o.output(sf, output='..\\test30.csv')

    print(_ret)
    # correct output
    """
    True
    """

    print('--- test 30a ends ---')

def test31():
    outputscheme = '1'
    print('test 31 checks split output to csv')
    print('---- testing 31 begins ----')

    sf = projectloader('test\\test31', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    o = pluginnamespace()['CSV']()

    _ret = o.output(sf, output='..\\test31.csv')

    print(_ret)
    # correct output
    """
    True
    """

    print('--- test 31 ends ---')

def test32():
    outputscheme = '1'
    print('test 32 checks method injection')
    print('---- testing 32 begins ----')

    sf = projectloader('test\\test32', dbg=False, outputscheme=outputscheme)

    x = sf.dataasobject

    print('--- explore results ---')

    print(x)

    print('--- test 32 ends ---')

def test33():
    outputscheme = '1'
    print('test 33 checks if all methods work')
    print('---- testing 33 begins ----')

    sf = projectloader('test\\test33\\', dbg=False, outputscheme=outputscheme)

    x = sf.dataasobject

    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    for row in _ret:
        print(row)

    print('--- test 33 ends ---')


    #expected output
    """
    test 33 checks method inclusion in output using a format string
    ---- testing 33 begins ----
    loading plug-in: choice
    loading plug-in: combine
    loading plug-in: csv
    loading plug-in: dummy
    loading plug-in: enum
    loading plug-in: excel
    loading plug-in: filename
    loading plug-in: fullpath
    loading plug-in: grid
    loading plug-in: json
    loading plug-in: math
    loading plug-in: number
    loading plug-in: parent
    loading plug-in: path
    loading plug-in: real
    loading plug-in: ref
    loading plug-in: static
    loading plug-in: string
    loading plug-in: url
    loading plug-in: yaml
    Registering Dynamic Class: CLASSONE
    --- explore results ---
    ['num1', 'num2', 'text1', 'test1', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7', 'test8', 'test9', 'test10', 'test11']
    ['10', '20', 'High', '30', '60', 'tf1.txt', 'test\test33\\data', 'test\test33\\data\tf1.txt', '*', '10 % 20', 'THIS IS STATICA!!', '3', 'High', '3']
    ['15', '25', 'High', '40', '80', 'tf2.txt', 'test\test33\\data', 'test\test33\\data\tf2.txt', '*', '15 % 25', 'THIS IS STATICA!!', '3', 'High', '3']
    --- test 33 ends ---


    """

def test34():
    outputscheme = '1'
    print('test 34 checks if method "use before declaration" works')
    print('---- testing 34 begins ----')

    sf = projectloader('test\\test34', dbg=False, outputscheme=outputscheme)

    x = sf.dataasobject

    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    for row in _ret:
        print(row)

    print('--- test 34 ends ---')

    # expected output
    """
    test 34 checks if method "use before declaration" works
    ---- testing 34 begins ----
    loading plug-in: choice
    loading plug-in: combine
    loading plug-in: csv
    loading plug-in: dummy
    loading plug-in: enum
    loading plug-in: excel
    loading plug-in: filename
    loading plug-in: fullpath
    loading plug-in: grid
    loading plug-in: json
    loading plug-in: math
    loading plug-in: number
    loading plug-in: parent
    loading plug-in: path
    loading plug-in: real
    loading plug-in: ref
    loading plug-in: static
    loading plug-in: string
    loading plug-in: url
    loading plug-in: yaml
    Registering Dynamic Class: CLASSONE
    Error in Math Plugin config: In CLASSONE a method called test1 is being consumed before it is initialized. Make sure you declare your methods in order.

    Process finished with exit code 1
    """

def test35():
    outputscheme = '1'
    print('test 35 validates new header system works for grid output')
    print('---- testing 35 begins ----')

    sf = projectloader('test\\test35', dbg=False, outputscheme=outputscheme)

    """
    try:
        checkalignment(sf)
    except ValueError as err:
        print(err)
        sys.exit(1)
    """
    print('--- explore results ---')

    o = pluginnamespace()['GRID']()

    _ret = o.output(sf)

    _ret.trim()

    for row in _ret:
        print(row)

    # correct output
    """
    --- explore results ---
    ['A_p1', 'A_p2', 'B_p1', 'B_p2', 'B_p3', 'C_p1', 'C_p2', 'C_p3']
    ['d1 ipsum lorum horus', 'hello world', 'subc1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', 'subb1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    ['d1 ipsum lorum horus', 'hello world', 'subc1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0', 'subb1 ipsum lorum horus', 'alpha beta\nipsum lorum horus rictum', '4.0']
    --- test 35 ends ---
    """

    print('--- test 35 ends ---')

def test36():
    outputscheme = '1'
    print('test 36 validates format string system, including headers, works for tree output')
    print('---- testing 36 begins ----')

    sf = projectloader('test\\test36\\', dbg=False, outputscheme=outputscheme)

    print('--- explore results ---')

    o = pluginnamespace()['JSON']()

    _ret = o.output(sf)

    print(_ret)

    # output should not include attributes ending in "2"
    # correct output
    """
    ---- testing 36 begins ----
    loading plug-in: choice
    loading plug-in: combine
    loading plug-in: csv
    loading plug-in: dummy
    loading plug-in: enum
    loading plug-in: excel
    loading plug-in: filename
    loading plug-in: fullpath
    loading plug-in: grid
    loading plug-in: json
    loading plug-in: math
    loading plug-in: number
    loading plug-in: parent
    loading plug-in: path
    loading plug-in: real
    loading plug-in: ref
    loading plug-in: static
    loading plug-in: string
    loading plug-in: url
    loading plug-in: yaml
    Registering Dynamic Class: SUBB
    Registering Dynamic Class: SUBA
    Registering Dynamic Class: SUBC
    --- explore results ---
    [
        {
            "suba1": {
                "testpropa1": "d1 ipsum lorum horus",
                "testpropa3": {
                    "testpropb1": "subc1 ipsum lorum horus",
                    "testpropb3": 4.0
                },
                "testpropa4": {
                    "testpropc1": "subb1 ipsum lorum horus",
                    "testpropc3": 4.0
                }
            }
        },
        {
            "suba2": {
                "testpropa1": "d1 ipsum lorum horus",
                "testpropa3": {
                    "testpropb1": "subc1 ipsum lorum horus",
                    "testpropb3": 4.0
                },
                "testpropa4": {
                    "testpropc1": "subb1 ipsum lorum horus",
                    "testpropc3": 4.0
                }
            }
        }
    ]
    --- test 36 ends ---
    """
    print('--- test 36 ends ---')

def test37():
    outputscheme = '1'
    print('test 37 checks if all methods work for tree output')
    print('---- testing 37 begins ----')

    sf = projectloader('test\\test37', dbg=False, outputscheme=outputscheme)

    x = sf.dataasobject

    print('--- explore results ---')

    o = pluginnamespace()['JSON']()

    _ret = o.output(sf)

    print(_ret)

    print('--- test 37 ends ---')


    #expected output
    """
    test 37 checks if all methods work for tree output
    ---- testing 37 begins ----
    loading plug-in: choice
    loading plug-in: combine
    loading plug-in: csv
    loading plug-in: dummy
    loading plug-in: enum
    loading plug-in: excel
    loading plug-in: filename
    loading plug-in: fullpath
    loading plug-in: grid
    loading plug-in: json
    loading plug-in: math
    loading plug-in: number
    loading plug-in: parent
    loading plug-in: path
    loading plug-in: real
    loading plug-in: ref
    loading plug-in: static
    loading plug-in: string
    loading plug-in: url
    loading plug-in: yaml
    Registering Dynamic Class: CLASSONE
    --- explore results ---
    [
        {
            "tf1": {
                "num1": 10,
                "num2": 20,
                "test1": 30,
                "test10": "High",
                "test11": 3,
                "test2": 60,
                "test3": "tf1.txt",
                "test4": "test\test37\\data",
                "test5": "test\test37\\data\tf1.txt",
                "test6": "*",
                "test7": "10 % 20",
                "test8": "THIS IS STATICA!!",
                "test9": 3,
                "text1": "High"
            }
        },
        {
            "tf2": {
                "num1": 15,
                "num2": 25,
                "test1": 40,
                "test10": "High",
                "test11": 3,
                "test2": 80,
                "test3": "tf2.txt",
                "test4": "test\test37\\data",
                "test5": "test\test37\\data\tf2.txt",
                "test6": "*",
                "test7": "15 % 25",
                "test8": "THIS IS STATICA!!",
                "test9": 3,
                "text1": "High"
            }
        }
    ]
    --- test 37 ends ---
    """

def test38():
    outputscheme = 'json' #not actually used
    print('test 38 tests node registry search')
    print('---- testing 38 begins ----')

    sf = projectloader('test\\test38', dbg=False, outputscheme=outputscheme)


    print('--- explore results ---')

    from gtool.core.noderegistry import getObjectByUri, \
        getObjectByUriElement, \
        getObjectByUriElementAndType, \
        getUrisByNodeType, \
        nodenamespace, \
        objectUri

    _x = sf.dataasobject

    nspace = nodenamespace().keys()

    print('--- registered objects by uri ---')

    for node in nspace:
        print(node)

    print('\n--- object by uri ---')

    print(getObjectByUri('/suba1/testpropa4'))

    print('\n--- object by node type ---')
    for uri in getUrisByNodeType('SUBB'):
        print(uri)

    print('\n--- object by uri element ---')

    objbyuri = getObjectByUriElement('test')
    for obj in objbyuri:
        print(objectUri(obj))

    print('\n--- object by uri and type ---')

    objbyuriandtype = getObjectByUriElementAndType('test', 'SUBC')
    for obj in objbyuriandtype:
        print(obj)

    print('\n--- object uri ---')

    for obj in objbyuriandtype:
        print(objectUri(obj))

    # correct output
    """
    test 38 tests node registry search
    ---- testing 38 begins ----
    loading plug-in: choice
    loading plug-in: combine
    loading plug-in: csv
    loading plug-in: dummy
    loading plug-in: enum
    loading plug-in: excel
    loading plug-in: filename
    loading plug-in: fullpath
    loading plug-in: grid
    loading plug-in: json
    loading plug-in: math
    loading plug-in: nodename
    loading plug-in: number
    loading plug-in: parent
    loading plug-in: path
    loading plug-in: real
    loading plug-in: ref
    loading plug-in: static
    loading plug-in: string
    loading plug-in: url
    loading plug-in: xattrib
    loading plug-in: yaml
    Registering Dynamic Class: SUBB
    Registering Dynamic Class: SUBA
    Registering Dynamic Class: SUBC
    --- explore results ---
    --- registered objects by uri ---
    /suba2/testpropa4
    /suba1/testpropa3
    /suba1/testpropa4
    /suba1
    /suba2/testpropa3
    /suba2

    --- object by uri ---
    SUBC: {'testpropc1': [subb1 ipsum lorum horus], 'testpropc3': [4.0], 'testpropc2': [alpha beta, ipsum lorum horus rictum]}

    --- object by node type ---
    /suba1/testpropa3
    /suba2/testpropa3

    --- object by uri element ---
    /suba2/testpropa4
    /suba1/testpropa3
    /suba1/testpropa4
    /suba2/testpropa3

    --- object by uri and type ---
    SUBC: {'testpropc1': [subb1 ipsum lorum horus], 'testpropc3': [4.0], 'testpropc2': [alpha beta, ipsum lorum horus rictum]}
    SUBC: {'testpropc1': [subb1 ipsum lorum horus], 'testpropc3': [4.0], 'testpropc2': [alpha beta, ipsum lorum horus rictum]}

    --- object uri ---
    /suba2/testpropa4
    /suba1/testpropa4
    --- test 38 ends ---
    """


def test39():
    outputscheme = '1'
    print('test 39 checks if all xattrib method plugin works')
    print('---- testing 39 begins ----')

    sf = projectloader('test\\test39\\', dbg=False, outputscheme=outputscheme)

    x = sf.dataasobject

    print('--- explore results ---')

    o = pluginnamespace()['JSON']()

    _ret = o.output(sf)

    print(_ret)

    print('--- test 39 ends ---')


    #expected output
    """

    """

def test40():
    outputscheme = '1'
    print('test 40 checks if aggregator loading works')
    print('---- testing 39 begins ----')

    sf = projectloader('test\\test40\\', dbg=False, outputscheme=outputscheme)

    x = sf.dataasobject

    print('--- explore results ---')

    o = pluginnamespace()['JSON']()

    _ret = o.output(sf)

    print(_ret)

    from gtool.core.aggregatorregistry import aggregatornamespace

    print(aggregatornamespace().keys())

    print('--- test 40 ends ---')


    #expected output
    """
    test 40 checks if aggregator loading works
    ---- testing 39 begins ----
    loading plug-in: choice
    loading plug-in: combine
    loading plug-in: csv
    loading plug-in: dummy
    loading plug-in: enum
    loading plug-in: excel
    loading plug-in: filename
    loading plug-in: fullpath
    loading plug-in: grid
    loading plug-in: json
    loading plug-in: math
    loading plug-in: nodename
    loading plug-in: number
    loading plug-in: parent
    loading plug-in: path
    loading plug-in: real
    loading plug-in: ref
    loading plug-in: static
    loading plug-in: string
    loading plug-in: url
    loading plug-in: xattrib
    loading plug-in: yaml
    Registering Dynamic Class: CLASSONE
    --- explore results ---
    [
        {
            "tf1": {
                "num1": 10,
                "num2": 20,
                "test1": 30,
                "test2": 15,
                "test3": 15
            }
        },
        {
            "tf2": {
                "num1": 15,
                "num2": 25,
                "test1": 40,
                "test2": 15,
                "test3": 10
            }
        }
    ]
    dict_keys(['AVERAGE', 'LIST1', 'TOTAL23'])
    --- test 40 ends ---
    """