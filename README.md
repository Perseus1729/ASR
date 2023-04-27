# Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis

[Link to paper](https://arxiv.org/abs/1803.09017)

## Files

- Hyperparameters.py - for hyperparameter tuning
- Network.py - Encoder and Decoder classes
- Synthesis.py - Generates waveforms
- utils.py - Contains all other important functions

To generate waveform: Replace the text in generate.py with your test text and run it.

## Summary of Paper

### Method

The authors first introduce the architecture of the end-to-end speech synthesis system, which consists of an encoder that maps the input text to a continuous vector representation, and a decoder that generates the corresponding speech waveform. They then introduce the Style Token Layer, which is inserted between the encoder and decoder and is responsible for modeling and controlling the style of the synthesized speech.

The Style Token Layer consists of a set of learnable vectors, called Style Tokens, that capture different aspects of the speech style such as the speaker identity, emotional state, and speaking rate. These Style Tokens are learned in an unsupervised manner using an adversarial training procedure that encourages the system to generate speech that is both natural-sounding and diverse in terms of style.

During training, the encoder is trained to produce a fixed-length vector representation of the input text, which is then concatenated with a randomly selected subset of the Style Tokens. The concatenated vector is then passed through the decoder to generate the corresponding speech waveform. The decoder is trained to reconstruct the original waveform from the concatenated vector.

During inference, the user can control the style of the synthesized speech by selectively activating or deactivating different Style Tokens. For example, the user can specify the speaker identity by activating the corresponding Style Token while deactivating other Style Tokens.

### Experiments

This section presents the experimental setup used to evaluate the proposed approach and provides the results of the experiments. The authors use the LJ Speech dataset, which consists of 13,100 short audio clips of a single speaker reading passages from a book. They evaluate the proposed approach using both objective measures such as the Mel Cepstral Distortion (MCD) and subjective measures such as Mean Opinion Score (MOS).

The experiments show that the proposed approach outperforms existing approaches in terms of both objective and subjective evaluations. The synthesized speech is shown to be more natural-sounding and diverse in terms of style.

### Possible Modifications

1. The proposed approach uses a set of learnable vectors to represent different aspects of speech style. We could try using a set of discrete labels to represent different speakers or emotions, or use a continuous vector to represent the speaking rate.

   To train the model with discrete labels, you could use a classification-based approach. You would first train a classifier network to predict the style labels from the input speech data. Then, you could extract the feature representations from the classifier network and use them as the Style Tokens.

2. Exporting this idea from speech files to images. We can apply one style of images in terms of another image while preserving its content. In the image domain, we can extract features from images using deep neural networks, which learn to extract high-level features, i.e we can use CNN's.

3. In the Style Tokens paper, the authors use a method called "randomized subset selection" to select a smaller subset of style tokens from the full set of style tokens. We can reduce the number of style tokens, by using methods like PCA and K-means clustering to further identify the similarity between the Style tokens that are being used.

## CS 753 Hacker Project

### Team Members

1. Punna Hitesh Kumar (190050093)
2. Dasari Heemmanshu (190050029)


Paper: Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis
Link: https://arxiv.org/abs/1803.09017 

Files: 
- Hyperparameters.py: for hyperparameter tuning
- Network.py: Encoder and Decoder classes
- Synthesis.py: Generates waveforms
- utils.py: Contains all other important functions

To generate waveform: Replace the text in generate.py with your test text and run it. 

Summary of Paper:
- Method: The authors first introduce the architecture of the end-to-end speech synthesis system, which consists of an encoder that maps the input text to a continuous vector representation, and a decoder that generates the corresponding speech waveform. They then introduce the Style Token Layer, which is inserted between the encoder and decoder and is responsible for modeling and controlling the style of the synthesized speech.
- The Style Token Layer consists of a set of learnable vectors, called Style Tokens, that capture different aspects of the speech style such as the speaker identity, emotional state, and speaking rate. These Style Tokens are learned in an unsupervised manner using an adversarial training procedure that encourages the system to generate speech that is both natural-sounding and diverse in terms of style.
- During training, the encoder is trained to produce a fixed-length vector representation of the input text, which is then concatenated with a randomly selected subset of the Style Tokens. The concatenated vector is then passed through the decoder to generate the corresponding speech waveform. The decoder is trained to reconstruct the original waveform from the concatenated vector.
- During inference, the user can control the style of the synthesized speech by selectively activating or deactivating different Style Tokens. For example, the user can specify the speaker identity by activating the corresponding Style Token while deactivating other Style Tokens.

Experiments: This section presents the experimental setup used to evaluate the proposed approach and provides the results of the experiments. The authors use the LJ Speech dataset, which consists of 13,100 short audio clips of a single speaker reading passages from a book. They evaluate the proposed approach using both objective measures such as the Mel Cepstral Distortion (MCD) and subjective measures such as Mean Opinion Score (MOS).
The experiments show that the proposed approach outperforms existing approaches in terms of both objective and subjective evaluations. The synthesized speech is shown to be more natural-sounding and diverse in terms of style.

Possible Modifications:
1. The proposed approach uses a set of learnable vectors to represent different aspects of speech style, we could try using a set of discrete labels to represent different speakers or emotions, or use a continuous vector to represent the speaking rate. To train the model with discrete labels, you could use a classification-based approach. You would first train a classifier network to predict the style labels from the input speech data. Then, you could extract the feature representations from the classifier network and use them as the Style Tokens.
2. Exporting this idea from speech files to images, i.e we try to apply one style of images in terms of another image while preserving it's content. In the speech domain, we extract features such as Mel-spectrograms. In the image domain, we can extract features from images using deep neural networks, which learn to extract high-level features, i.e we can use CNN's.
3. In the Style Tokens paper, the authors use a method called "randomized subset selection" to select a smaller subset of style tokens from the full set of style tokens. This is done in order to reduce the computational cost of training the model, while still maintaining the ability to model a diverse set of style variations. We can reduce the number of style tokens by using methods like PCA and K-means clustering to further identify the similarity between


Paper: Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis
Link: https://arxiv.org/abs/1803.09017 

Files: 
Hyperparameters.py - for hyperparameter tuning
Network.py - Encoder and Decoder classes
Synthesis.py - Generates waveforms
utils.py - Contains all other important functions

To generate waveform: Replace the text in generate.py with your test text and run it. 

Summary of Paper:-
Method: The authors first introduce the architecture of the end-to-end speech synthesis system, which consists of an encoder that maps the input text to a continuous vector representation, and a decoder that generates the corresponding speech waveform. They then introduce the Style Token Layer, which is inserted between the encoder and decoder and is responsible for modeling and controlling the style of the synthesized speech.

The Style Token Layer consists of a set of learnable vectors, called Style Tokens, that capture different aspects of the speech style such as the speaker identity, emotional state, and speaking rate. These Style Tokens are learned in an unsupervised manner using an adversarial training procedure that encourages the system to generate speech that is both natural-sounding and diverse in terms of style.

During training, the encoder is trained to produce a fixed-length vector representation of the input text, which is then concatenated with a randomly selected subset of the Style Tokens. The concatenated vector is then passed through the decoder to generate the corresponding speech waveform. The decoder is trained to reconstruct the original waveform from the concatenated vector.

During inference, the user can control the style of the synthesized speech by selectively activating or deactivating different Style Tokens. For example, the user can specify the speaker identity by activating the corresponding Style Token while deactivating other Style Tokens.

Experiments: This section presents the experimental setup used to evaluate the proposed approach and provides the results of the experiments. The authors use the LJ Speech dataset, which consists of 13,100 short audio clips of a single speaker reading passages from a book. They evaluate the proposed approach using both objective measures such as the Mel Cepstral Distortion (MCD) and subjective measures such as Mean Opinion Score (MOS).
The experiments show that the proposed approach outperforms existing approaches in terms of both objective and subjective evaluations. The synthesized speech is shown to be more natural-sounding and diverse in terms of style.

Possible Modifications:-
1.The proposed approach uses a set of learnable vectors to represent different aspects of speech style, we could try using a set of discrete labels to represent different speakers or emotions, or use a continuous vector to represent the speaking rate.
i.e Instead of learning continuous vectors through adversarial training, you would need to encode the different style aspects as a set of discrete labels or categories. For example, you could assign a different label to each speaker in the dataset, or use a set of emotion labels to represent different emotional states.

To train the model with discrete labels, you could use a classification-based approach. You would first train a classifier network to predict the style labels from the input speech data. Then, you could extract the feature representations from the classifier network and use them as the Style Tokens.

2.Exporting this idea from speech files to images, i.e we try to apply one style of images in terms of another image while preserving it's content
i.e In the speech domain, we extract features such as Mel-spectrograms, In the image domain, we can extract features from images using deep neural networks, which learn to extract high-level features, i.e we can use CNN's 

3.In the Style Tokens paper, the authors use a method called "randomized subset selection" to select a smaller subset of style tokens from the full set of style tokens. This is done in order to reduce the computational cost of training the model, while still maintaining the ability to model a diverse set of style variations.

We can reduce the number of style tokens, by using methods like PCA and K-means to clustering to further identify the similarity between the  Style tokens that are being used.


CS 753 Hacker Project
Team Members:
1) Punna Hitesh Kumar ( 190050093 )
2) Dasari Heemmanshuu ( 190050029 )
