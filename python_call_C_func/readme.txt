python setup.py build -cmingw32



1. �إ�.c��(ex: hello_0.c)
    (1). �s�WAPI ( ex: static PyObject* PyCallCtest(PyObject* self, PyObject* args) ) 
    (2). �إ�initial Method 
         PyMODINIT_FUNC inithelloTest(void) 
    (3). �إ�Method list
         static PyMethodDef HelloMethods[] = {
             {"pyCalltest", PyCallCtest, METH_VARARGS, "A test function."},
             {"PyListtest", PyListtest , METH_VARARGS, "A test function."},
             {NULL, NULL, 0, NULL}
         };
2. �إ�steup.py
3. ���� python setup.py build -cmingw32



http://0w0.logdown.com/posts/36859-python-c-api-p1
http://stackoverflow.com/questions/23355879/calling-c-function-from-python

http://book.pythontips.com/en/latest/python_c_extension.html