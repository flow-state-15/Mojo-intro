# Tiny performance tests between Python and Mojo languages

Mojo is a new language released in 2023. For now Modular has released it under
a [modified Business Source
License](https://www.modular.com/legal/max-mojo-license). It is under an
incubation period right now, but [the developers are progressively releasing the
language under the Apache 2
license](https://www.modular.com/blog/the-next-big-step-in-mojo-open-source).

> Will Mojo ever be fully open source?
>
> Yes. We remain strong believers in the importance of open-source software to
> accelerating innovation and are deeply committed to progressively make
> source code of Mojo fully available over time.

What's interesting about Mojo? It is a systems programming language that is a
superset of Python. As a language using JIT and AOT compilation, it is not
interpreted and does not suffer from that performance overhead. Imagine the easy
syntax of Python with the performance of C!

Hopefully this language takes off. It has so much potential.

## To run these tests yourself

You'll need to install the Magic virtual environment manager. [Here are the full
instructions](https://docs.modular.com/mojo/manual/get-started).

```py
curl -ssL https://magic.modular.com/4d9228ea-daf9-440c-ab17-76018455e050 | bash
```

Init the project:

```py
magic init mojo-intro --format mojoproject
```

`--format mojoproject` inits the project with the MAX framework dependency. Full
disclosure - [it collects telemetry
data](https://docs.modular.com/max/faq#why-bundle-mojo-with-max) - but MAX
allows Mojo to run on your GPU if you need that. The introductory vision of
this language is to be the industry language for AI algorithm development, so
the MAX framework does make sense here.

To run a file, use the familiar syntax `mojo <filename.mojo>`. This method uses
JIT compilation which is slightly slower than compiling directly to binary. To compile
Ahead Of Time, use `mojo build <filename>.mojo`.

To run both python and mojo files for comparisons (you'll need Python installed), try combining the commands:

```bash
python3 hello.py && mojo hello.mojo
```

I'll keep building out this repo since Mojo seems to be a fun advancement in our
industry. Feel free to clone and contribute your own findings!
