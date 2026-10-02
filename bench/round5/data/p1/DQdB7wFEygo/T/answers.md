# Answers — transcript-only arm (DQdB7wFEygo)

Evidence base: transcript.txt only, plus general knowledge. No frames were viewed; anything visual is marked as such.

## 1. In what kind of application is the code shown, and what visual theme does it use?

**Answer:** The code is shown in **Visual Studio Code**. Visual theme: **insufficient evidence**.

**Evidence:**
- Transcript says: [03:19]–[03:23] "step three set up Docker on your IDE of choice I'm doing vs code because I hate myself" and [03:25] "make sure to download the docker extension on your IDE". This states the editor directly.
- Theme (dark/light, which colour scheme) is purely visual and never mentioned in the transcript. Not determinable from transcript.

## 2. Is a full-screen titled slide shown at any point? Quote its title exactly.

**Answer:** **insufficient evidence**.

**Evidence:**
- The transcript is spoken narration; whether any frame is a full-screen titled slide cannot be determined from it. The narration is structured as numbered steps ("step one download Docker" [02:56]–[02:58], "step two check if you have Docker" [03:10]–[03:11], ... "step 10 Docker build Cloud" [10:53]–[10:54]), which in this creator's style (inference, general knowledge) are often shown as on-screen titles, but I cannot confirm any slide exists or quote an exact title.

## 3. What port number is set in the Dockerfile shown on screen?

**Answer:** **insufficient evidence**.

**Evidence:**
- Transcript confirms a port is set but never speaks the number: [05:50]–[05:55] "in our code we have this port environment variable we need to add this into our darker file we can do that with the EnV command", [05:57]–[06:01] "since this environment variable is a port we're also going to need this command this basically tells Docker hey we're going to need this port" (i.e. ENV and EXPOSE instructions). The `docker run -p` discussion [06:56]–[07:07] also gives no number.
- General knowledge: Node tutorials commonly use 3000 or 8080, but that is a guess, not evidence.

## 4. A .dockerignore file is shown. What does it contain?

**Answer:** At least **`node_modules`**. Whether anything else is in the file: **insufficient evidence**.

**Evidence:**
- Transcript: [05:43]–[05:48] "we can do that with a Docker ignore file and inside that file we're going to add the node modules folder and any other files you don't want in there". The transcript states node_modules is added; the phrase "any other files you don't want" leaves open whether additional entries were typed on screen.

## 5. What files and folders appear in the project's file explorer?

**Answer:** **insufficient evidence** for the exact on-screen list. From the transcript, the project is a simple Node server and at some point contains: a Dockerfile, a .dockerignore, package files (package.json, likely package-lock.json), a node_modules folder, a server source file (name unknown), and later a compose YAML file. Which of these are visible in the explorer at any given moment, and their exact names, cannot be confirmed.

**Evidence (transcript):**
- "here we have a simple node server" [03:38]; "first we're going to create the docker file" [03:42].
- "this First Command copies our package files" [04:55] (package.json / lock file, inferred from "package files").
- "we're copying our node modules" [05:36]; ".dockerignore" [05:43]–[05:47].
- "create a composed. yo file" [09:20]–[09:21] (transcription of "compose.yaml", inferred).
- The server filename (e.g. index.js / server.js) and any other explorer entries are never spoken.

Files read: questions.md, transcript.txt
