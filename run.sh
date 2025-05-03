# Now that we have set up both the backend and frontend, 
# you can start the application by following these steps:
# First, start the backend server:

cd /Users/zeyichen/Documents/研二spring/user_interface/arxiv_recommender/backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


# For the React frontend (original):
# In a new terminal, start the frontend development server:

# cd /Users/zeyichen/Documents/研二spring/user_interface/arxiv_recommender/frontend
# npm install
# npm start


# For the Streamlit frontend (recommended):
# In a new terminal, start the Streamlit frontend:

cd /Users/zeyichen/Documents/研二spring/user_interface/arxiv_recommender/frontend_streamlit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


# Alternatively, you can run both backend and Streamlit frontend with a single command:
# chmod +x run_streamlit.sh
# ./run_streamlit.sh


# for prime pods allocation
prime pods create \
--id 6bd7c8 \
--cloud-id massedcompute \
--gpu-type H100_80GB \
--gpu-count 1 \
--name test \
--disk-size 1250 \
--vcpus 20 \
--memory 128


prime pods create \
--id  54db25 \
--cloud-id nebius \
--gpu-type H100_80GB \
--gpu-count 1 \
--name test \
--disk-size 400 \
--vcpus 16 \
--memory 200

prime pods create \
--id  ecaddf \
--cloud-id hyperstack \
--gpu-type H100_80GB \
--gpu-count 2 \
--name test \
--disk-size 1500 \
--vcpus 60 \
--memory 360

# spot
prime pods create \
--id 6972a6 \
--cloud-id primecompute \
--gpu-type H100_80GB \
--gpu-count 8 \
--name test1 \
--disk-size 11096 \
--vcpus 104 \
--memory 752


prime pods create \
--id a49af3 \
--cloud-id hyperstack \
--gpu-type H100_80GB \
--gpu-count 8 \
--name test \
--disk-size 6500 \
--vcpus 252 \
--memory 1440

prime pods create \
--id ccc676 \
--cloud-id hyperstack \
--gpu-type H100_80GB \
--gpu-count 1 \
--name test \
--disk-size 750 \
--vcpus 28 \
--memory 180


prime availability list --gpu-type H100_80GB