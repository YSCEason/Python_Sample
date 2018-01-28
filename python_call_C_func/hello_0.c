#include <Python.h>
#include "inc_test.h"

// static PyObject *helloError;

static PyObject* PyCallCtest(PyObject* self, PyObject* args)
{

    int    iNum;
    double fNum;
    char*   str;
    int    array[3] = {0};

    if (!PyArg_ParseTuple(args, "ids", &iNum, &fNum, &str)) 
    {
        return NULL;
    }

    printf("%d\n", iNum);
    printf("%f\n", fNum);
    printf("%s\n", str);
    printf("--------------------------------------\n");
    
    int dd = 0;
    dd = inc_test(5);
    printf(">>>>>>>>>>>  %d\n",dd);

	array[0] = 11;
	array[1] = 22;
	array[2] = 33;

    printf("Hello! A C function called!\n");
    // Py_RETURN_NONE;  /* return None */

    return Py_BuildValue("[i, i, i]", array[0], array[1], array[2]);

    // return;
}

static PyObject* PyListtest(PyObject* self, PyObject* args)
{

    char *tok;          /* delimiter tokens for strtok */
    int cols;           /* number of cols to parse, from the left */
    int i = 0;

    int numLines;       /* how many lines we passed for parsing */
    char * line;        /* pointer to the line as a string */
    int inttest;

    PyObject * listObj; /* the list of strings */
    PyObject * strObj;  /* one string in the list */

    printf("----- PyListtest -----\n");
    
    /* the O! parses for a Python object (listObj) checked to be of type PyList_Type */
    if (! PyArg_ParseTuple( args, "O!is", &PyList_Type, &listObj, &cols, &tok )) 
        return NULL;
    
    /* get the number of lines passed to us */
    numLines = PyList_Size(listObj);
    
    /* should raise an error here. */
    if (numLines < 0) 
        return NULL; /* Not a list */

    /* iterate over items of the list, grabbing strings, and parsing for numbers */
    for (i=0; i<numLines; i++)
    {
        /* grab the string object from the next element of the list */
        strObj = PyList_GetItem(listObj, i); /* Can't fail */

        /* make it a string */

        if(PyString_Check(strObj))
        {
            line = PyString_AsString( strObj );
            printf(">>>> %s\n", line);
        }
        else if(PyInt_Check(strObj))
        {
            inttest = PyInt_AsLong( strObj );
            printf(">>>> %d\n", inttest);
        }

        /* now do the parsing */



    }

    printf(">> %d\n", cols);
    printf(">> %s\n", tok);

    printf("----- END -----\n");
    return Py_None;
}

static PyMethodDef HelloMethods[] = {
    {"pyCalltest", PyCallCtest, METH_VARARGS, "A test function."},
    {"PyListtest", PyListtest , METH_VARARGS, "A test function."},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC inithelloTest(void)
{
	PyObject *m;

	printf("inithello-------------\n");

    m = Py_InitModule("helloTest", HelloMethods);
    if(m == NULL) return;

    // helloError = PyErr_NewException("hello.error", NULL, NULL);
    // Py_INCREF(helloError);

    // PyModule_AddObject(m, "error", helloError);
}