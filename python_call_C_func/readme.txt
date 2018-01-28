python setup.py build -cmingw32



1. 建立.c檔(ex: hello_0.c)
    (1). 新增API ( ex: static PyObject* PyCallCtest(PyObject* self, PyObject* args) ) 
    (2). 建立initial Method 
         PyMODINIT_FUNC inithelloTest(void) 
    (3). 建立Method list
         static PyMethodDef HelloMethods[] = {
             {"pyCalltest", PyCallCtest, METH_VARARGS, "A test function."},
             {"PyListtest", PyListtest , METH_VARARGS, "A test function."},
             {NULL, NULL, 0, NULL}
         };
2. 建立steup.py
3. 執行 python setup.py build -cmingw32



http://0w0.logdown.com/posts/36859-python-c-api-p1
http://stackoverflow.com/questions/23355879/calling-c-function-from-python

http://book.pythontips.com/en/latest/python_c_extension.html