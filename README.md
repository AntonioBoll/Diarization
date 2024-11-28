# Diarization Repository
Welcome to the repository for the article "Beyond Audio Signals: Generative Model-Based Speaker Diarization in Portuguese".
This repository provides access to the code, prompts, and datasets used in the study.

The full paper can be accessed here.

Contents

1. Assembly
This section includes 8 dataset folders and general metrics for evaluating the Assembly model:

- Dataset folders:
Each folder contains:
* Baseline transcriptions (used for comparisons).
* Model-generated responses.
* Evaluation metrics: Accuracy, Precision, Recall, and F1 Score for both sentence-level and word-level transcriptions.
* General metrics for word-level evaluation: Contains the calculations for the overall metrics at the word level for the Assembly model.
* General metrics for sentence-level evaluation: Contains the calculations for the overall metrics at the sentence level for the Assembly model.

2. Dataset
This section includes 8 videos sourced from the Ordem do Dia sessions of Brazil's Chamber of Deputies.

- Each dataset folder includes:
* PDF documents.
* Audio recordings.
* Video files.
*Transcriptions.
* Metadata (number, date, and time of the session).

3. Oracle
Similar to the Assembly section, this includes 8 dataset folders and general metrics, with an additional focus on diarization using the Oracle model:

- Dataset folders:
Each folder contains:
* Baseline transcriptions (used for comparisons).
* Model-generated responses.
* Oracle JSON files (transcriptions and diarization data).
* Evaluation metrics: Accuracy, Precision, Recall, and F1 Score for both sentence-level and word-level transcriptions.
* General metrics for word-level evaluation: Contains the calculations for the overall metrics at the word level for the Oracle model.
* General metrics for sentence-level evaluation: Contains the calculations for the overall metrics at the sentence level for the Oracle model.

4. Ours
This section includes 8 dataset folders and general metrics for our proposed method:

- Dataset folders:
Each folder contains:

* Baseline transcriptions (used for comparisons).
* Model-generated responses.
* Evaluation metrics: Accuracy, Precision, Recall, and F1 Score for both sentence-level and word-level transcriptions.
* General metrics for word-level evaluation: Contains the calculations for the overall metrics at the word level for our method.
* General metrics for sentence-level evaluation: Contains the calculations for the overall metrics at the sentence level for our method.

5. Statistics
The Statistics folder includes:

* Confidence interval calculation code and results.
* Wilcoxon test calculation code and results.

6. Notebook for Tests
A comprehensive notebook is provided to:

* Run the diarization process.
* Include the prompts, code, and detailed steps to reproduce all results mentioned above.

This repository ensures transparency and reproducibility for researchers and practitioners working on speaker diarization in Portuguese.







This repository was created to make avaible the codes, prompts and datasets from the article "Beyond Audio Signals: Generative Model-Based Spekaer Diarization in Portuguese". 
This paper is avaible in this link: X

It consists of:

- Assembly:
There are 8 dataset folders and two general metrics.
* Dataset folders: There are 8 dataset folders. They consist of the baseline transcription used to compare the results from the model, the model answer, and the Accuracy, Precision, Recall and F1 Score for both the sentence and the word level transcriptions.
* General metrics for word level evaluation: They show the math done to get the general metrics for the word level evaluation on the Assembly model.
* General metrics for sentence level evaluation: They show the math done to get the general metrics for the sentence level evaluation on the Assembly model.

- Dataset:
There are 8 videos obtained from the "Ordem do Dia" inside the Deputies Chamber from Brazil sessions.
Each folder contains the pdf, the audio, the video, the transcription and the number, day and time. All from the session.

- Oracle:
There are 8 dataset folders and two general metrics.
* Dataset folders: There are 8 dataset folders. They consist of the baseline transcription used to compare the results from the model, the model answer, the Oracle json file with the transcription and diarization, and the Accuracy, Precision, Recall and F1 Score for both the sentence and the word level transcriptions.
* General metrics for word level evaluation: They show the math done to get the general metrics for the word level evaluation on the Oracle model.
* General metrics for sentence level evaluation: They show the math done to get the general metrics for the sentence level evaluation on the Oracle model.
  
- Ours:
There are 8 dataset folders and two general metrics.
* Dataset folders: There are 8 dataset folders. They consist of the baseline transcription used to compare the results from the model, the model answer, and the Accuracy, Precision, Recall and F1 Score for both the sentence and the word level transcriptions.
* General metrics for word level evaluation: They show the math done to get the general metrics for the word level evaluation on our method.
* General metrics for sentence level evaluation: They show the math done to get the general metrics for the sentence level evaluation on our method.

- Statistics:
The statistics folder consist of the Confidence Interval code calculations, the Confidence Interval results, the Wilcox text code calculations and the Wilcox results.

- Notebook for tests:
At last, there is a notebook to run the diarization, with the prompts, code and every step made to reproduce the results above.
