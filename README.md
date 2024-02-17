# cvcoach
build a coach to help candidate to highlight their experience. Most of the time we do great things but we don't know how to tell them.

# package streamlit-pydantic
this package helps to generate streamlit from a pydantic Basemodel (https://github.com/LukasMasuch/streamlit-pydantic/tree/main)
But this version doesn't support the pydantic version 2.6.1.

If you are installing streamlit-pydantic (pip install streamlit-pydantic) you have to modify the source file as follow :

- Before install the pydantic migration package (https://docs.pydantic.dev/2.6/migration/) : pip install bump-pydantic 
- go to the source directory of streamlit-pydantic "/opt/anaconda3/envs/ocr_cv/lib/python3.11/site-packages/"
- bump-pydantic streamlit_pydantic
- pip install pydantic-settings

Now it should work
