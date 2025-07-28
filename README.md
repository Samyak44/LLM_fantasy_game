# LLM_fantasy_game
Fine-tuning Gpt-2

What was the training for?
Fine-tuned GPT-2, a powerful language model, on your custom dataset of fantasy-themed names and titles like:
•	AshBorn the Molten
•	BlazeClawKnight
•	DragonFlame the Charred
•	SmolderStormChampion
•	WildWrathWarrior
 Goal of Fine-tuning
Trained GPT-2 to learn and generate similar fantasy names, titles, and combinations by:
•	Understanding common prefixes (Ash, Blaze, Cinder, Dragon, Fury, etc.)
•	Combining them with roles (Hunter, Reaper, Knight, etc.)
•	And adding epic adjectives (the Charred, the Infernal, the Blazing)

Why fine-tune GPT-2 on this?
Fine-tuning helps GPT-2 become specialized in your domain. It allows:
•	Higher quality, thematically consistent outputs
•	Less randomness, more fitting names
•	Better autocomplete for fantasy RPGs, games.
Fantasy Name Generator (GPT-2 Fine-Tuned)
This project fine-tunes a GPT-2 language model to generate fantasy names (for characters, places, races, etc.) using a custom dataset. 

It includes:

Training on a fantasy names dataset
Saving the model
Deploying a FastAPI-based API to generate new names on the fly


 What This Project Does ?

Fine-tunes a GPT-2 model on a list of ~1000 fantasy-style names
Saves the trained model locally
Deploys an API with endpoints to:
Check status (/status)
Generate new names based on prompts (/generate?prompt=Ash)

Google Colab
First need to run the training model in Google colab. 
•	Upload your dataset (e.g., fantasy_names_1000.txt)
•	Run fine-tuning code (see Colab notebook) Get the API key to run the code from wandb.
•	Download or save model to Google Drive
•	Now will be able to run the model on Vs-code and check the API.


How to Run It
Local Setup
Bash,Copy
git clone https(https://github.com/Samyak44/LLM_fantasy_game/)
cd fantasy-gpt2-api
pip install -r requirements.txt
Ensure you’ve already fine-tuned the model and saved it under fantasy-gpt2-model/.
The model was about 1.5 gb therefore need to download the model from google colab file.

Then run:

bash
Copy
uvicorn app:app --reload
Now go to:

http://127.0.0.1:8000/status
http://127.0.0.1:8000/generate?prompt=Ash

Result: On average, the model’s loss during training was 0.9934 below 1 — a decent value for text generation. Lower is generally better. Epoch was 3 therefore model saw your dataset 3 times in total.
The loss of ~0.99 indicates that your fine-tuned model learned some structure in your fantasy name dataset.
Since we only trained for 3 epochs on 1,000 names, it’s enough to generate fantasy-like names, 

What I'd Improve with More Time/Resources
Use LoRA or PEFT to reduce training cost
Add UI (streamlit or HTML) to make a front-end.
Expose model on Hugging Face Spaces or Render.
Include more diverse datasets (e.g., race names, city names, descriptions)

<img width="468" height="636" alt="image" src="https://github.com/user-attachments/assets/af68f108-cd78-4b06-a30a-f4a93f7ea821" />
