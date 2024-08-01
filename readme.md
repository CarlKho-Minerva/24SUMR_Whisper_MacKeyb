# Whisper Transcription App

This project is a transcription application that uses OpenAI's Whisper API to transcribe audio recordings. The application records audio, saves it to a temporary file, transcribes the audio, and copies the transcription to the clipboard. You can trigger the transcription process by pressing `cmd+r`.

## Project Structure

```plaintext
.env
.gitignore
com.user.whisptertranscription.plist
venv/
    bin/
        activate
        activate.csh
        activate.fish
        Activate.ps1
        ...
    include/
        python3.12/
    lib/
        python3.12/
            site-packages/
                ...
    pyvenv.cfg
whisper_transcription_app.py
```

## Prerequisites

- Python 3.12
- Virtual environment ([`venv`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fcvk%2FDownloads%2F%5BCODE%5D%20Local%20Projects%2F24SUMR_Whisper_on_opt-W_Mac%2Fvenv%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/cvk/Downloads/[CODE] Local Projects/24SUMR_Whisper_on_opt-W_Mac/venv"))
- OpenAI API key

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/CarlKho-Minerva/24SUMR_Whisper_MacKeyb
    cd https://github.com/CarlKho-Minerva/24SUMR_Whisper_MacKeyb
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add your OpenAI API key:

    ```env
    OPEN_AI_API=your_openai_api_key
    ```

## Usage

1. **Run the application:**

    ```sh
    python whisper_transcription_app.py
    ```

2. **Record and transcribe audio:**

    The application will record audio, save it to a temporary file, transcribe the audio using OpenAI's Whisper API, and copy the transcription to the clipboard.

## File Descriptions

- **[whisper_transcription_app.py](whisper_transcription_app.py):** Main application script that handles audio recording, saving, transcription, and clipboard copying.
- **[venv/bin/Activate.ps1](venv/bin/Activate.ps1):** PowerShell script for activating the virtual environment.
- **[venv/bin/activate](venv/bin/activate):** Bash script for activating the virtual environment.
- **[.env](.env):** Environment variables file (not included in the repository, to be created by the user).
- **[.gitignore](.gitignore):** Git ignore file to exclude certain files and directories from version control.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for providing the Whisper API.
- The Python community for various libraries used in this project.

## Contact

For any questions or issues, please open an issue in the repository or contact the maintainer.
