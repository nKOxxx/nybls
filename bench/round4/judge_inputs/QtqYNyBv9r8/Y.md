1. Page header bar (inside the page): "The Rust Programming Language". Address bar domain:
   doc.rust-lang.org (path at 04:35: /book/ch01-03-hello-cargo.html). The Chrome window
   title at that moment reads "Hello, Cargo! - The Rust Programming Language - Google
   Chrome" (chapter specific; the in page header is the constant one).
   Evidence: z_275000_0_0_34 [04:35] (seen); header text visible in every browser tile of
   sheet_000 [00:39 to 06:38] and sheet_001 [06:58 to 11:38].

2. Branch: master. Prompt reads hello_cargo git:(master) x after cd hello_cargo. Yes, the
   VS Code status bar also shows it: "master*" at bottom left.
   Evidence: z_275000_50_3_50 [04:35] for the prompt (seen). z_586000_50_95_50 [09:46] for
   the status bar (seen). Caveat (inferred): the 09:46 VS Code window appears to be the
   later guessing_game project, not hello_cargo; the branch name shown is nonetheless
   "master", the same name.

3. Hello, wolrd! (transposed letters "wolrd", a typo in the source, not a misread; the
   tighter zoom confirms l before r).
   Evidence: z_275000_50_3_50 and z_275000_50_3_20 [04:35], terminal scrollback showing
   hello_world ./main followed by the output line (seen).

4. cargo 1.88.0 (873a06493 2025-05-10). Evidence: z_275000_50_3_50 [04:35] (seen).

5. Command typed at prompt release git:(master) x: . ./hello_cargo (sourcing the compiled
   binary with the dot builtin; the shell immediately prints [2] 62750).
   Final job status line: [2]  + 62750 exit 127   ELF   > (job number 2, PID 62750, exit
   code 127; "ELF >" is the mangled job text).
   Evidence: z_418000_50_0_50 [06:58] for the command and the [2] 62750 line (seen);
   z_418000_50_44_50 [06:58] for the tail and job status line (seen). Location came from
   sheet_001 tile [06:58] showing the flood (seen).
