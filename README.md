# Hey, I'm Ash — I Love Building Infrastructure

- Building [Unum Cloud](https://unum.cloud) since 2015.
- Computer Science & AI researcher (unpublished, by choice).
- Twice an Astrophysics dropout, lifelong Bioinformatics fan.
- Investing in deep-tech, cloud, & semiconductors.
- Fluent in English, Russian & Armenian.
- Lived in 🇺🇸🇬🇧🇷🇺🇦🇲 & 🇲🇽🇵🇦🇦🇷🇩🇪🇦🇪🇹🇭🇲🇾🇻🇳🇮🇩.
- Frequent host of "Systems" meetups in [Armenia](https://github.com/cpp-armenia/meetings), and beyond.

For ~20 years, I've been coding in C++, CUDA, and Python — optimizing Assembly on x86 & ARM.
Prefer spaces over tabs, and use east-const and procedural code over OOP or functional abstractions.

__Want to chat?__
I'm __`@ashvardanian`__ on [GitHub](https://github.com/ashvardanian), [LinkedIn](https://linkedin.com/in/ashvardanian), [Twitter](https://twitter.com/ashvardanian), [Facebook](https://fb.com/ashvardanian), and [YouTube](https://youtube.com/playlist?list=PL2kcrNAeGTFzZbccNB3P_xruYPskMmwRT).
For venture, reach me at ash@aal.vc 🤗

[![GitHub Org's stars: Unum-Cloud](https://img.shields.io/github/stars/unum-cloud?style=social&label=Unum%20Stars)](https://github.com/unum-cloud)
[![GitHub User's stars: AshVardanian](https://img.shields.io/github/stars/ashvardanian?style=social&label=Personal%20Stars)](https://github.com/ashvardanian)
[![HackerNews User Karma](https://img.shields.io/hackernews/user-karma/ashvardanian?label=HackerNews)](https://ashvardanian.com/about#hackernews) <br/>
[![USearch Python installs](https://static.pepy.tech/personalized-badge/usearch?period=total&units=abbreviation&left_color=black&right_color=blue&left_text=USearch%20Python%20installs)](https://github.com/unum-cloud/usearch)
[![SimSIMD Python installs](https://static.pepy.tech/personalized-badge/simsimd?period=total&units=abbreviation&left_color=black&right_color=blue&left_text=SimSIMD%20Python%20installs)](https://github.com/ashvardanian/simsimd)
[![StringZilla Python installs](https://static.pepy.tech/personalized-badge/stringzilla?period=total&units=abbreviation&left_color=black&right_color=blue&left_text=StringZilla%20Python%20installs)](https://github.com/ashvardanian/stringzilla)

## Repositories

- __[USearch](https://github.com/unum-cloud/USearch)__ - a universal search engine powering many databases, AI labs, and experiments in Natural Sciences. Compact C++ core with 10+ language bindings — 10–100× faster than Meta FAISS for vector search and far beyond Apache Lucene.
- __[StringZilla](https://github.com/ashvardanian/StringZilla)__ - SIMD, SWAR, and CUDA-accelerated string algorithms for search, matching, hashing, and sorting at Web Scale and Bioinformatics scale. Hundreds of hand-tuned kernels with manual multi-versioning, exposed to C, C++, Rust, Python, Swift, and JavaScript, up to 10× faster on CPUs and 100× faster on GPUs.
- __[SimSIMD](https://github.com/ashvardanian/SimSIMD)__ - an extensive collection of mixed-precision vector math kernels for C, Python, Rust, and JavaScript. Designed for linear algebra, scientific computing, statistics, information retrieval, and image processing, delivering consistent SIMD speedups over BLAS and NumPy on both x86 and ARM architectures.
- __[UCall](https://github.com/unum-cloud/UCall)__ - a kernel-bypass web server backend for C and Python built on io_uring. Achieves 70× higher throughput and 50× lower latency than FastAPI for real-time workloads, including serving compact AI models.
- __[UForm](https://github.com/unum-cloud/UForm)__ - tiny multimodal AI models with state-of-the-art parameter and data efficiency. Compatible with Python, JS, and Swift, serving as a lightweight alternative to OpenAI CLIP for on-device and server inference.
- __[ForkUnion](https://github.com/ashvardanian/ForkUnion)__ - ultra-low-latency parallelism library for Rust and C++. Avoids allocations, mutexes, and even Compare-And-Swap atomics — achieving up to 10× speedups over Rayon and TaskFlow.

Some of those are used in open-source databases, like [ClickHouse](https://github.com/ClickHouse/ClickHouse), [DuckDB](https://github.com/duckdb/duckdb), [TiDB](https://github.com/pingcap/tidb), [ScyllaDB](https://github.com/scylladb/scylladb), [yugabyteDB](https://github.com/yugabyte/yugabyte-db), [DragonflyDB](https://github.com/dragonflydb/dragonfly), [MemGraph](https://github.com/memgraph), [Vald](https://github.com/vdaas/vald), [Turso](https://github.com/tursodatabase/turso), LLM toolchains, like [LangChain](https://github.com/langchain-ai/langchain), [LlamaIndex](https://github.com/run-llama/semtools), [Microsoft SemanticKernel](https://github.com/microsoft/semantic-kernel), [Nomic AI GPT4All](https://github.com/nomic-ai/gpt4all), [Surf](https://github.com/deta/surf), and many other less "open" systems, such as backend infrastructure of major AI labs, government intelligence agencies, Hyper-scale cloud companies, Fortune 500, iOS and Android apps with 100M-1B MAU.
There are also some cool scientific datasets and HPC tutorials you can borrow:

- __[less_slow.cpp](https://github.com/ashvardanian/less_slow.cpp)__ - teaches a performance oriented mindset for C++, CUDA, PTX, and ASM
  - __[less_slow.rs](https://github.com/ashvardanian/less_slow.rs)__ - Rust adaptation with a focus on higher-level abstractions
  - __[less_slow.py](https://github.com/ashvardanian/less_slow.py)__ - Python adaptation with a focus on scripting & data-management
- __[SpaceV](https://github.com/ashvardanian/SpaceV)__ - 1 billion vectors from Microsoft SpaceV extended for usability
- __[USearchMolecules](https://github.com/ashvardanian/usearch-molecules)__ - 28 billion fingerprints for drug discovery, published with AWS

And more demos, benchmarks, and fun hackathon projects:

- [UStore](https://github.com/unum-cloud/UStore) - multimodal embedded database for C, C++, and Python designed around key-value stores
- [StringWars](https://github.com/ashvardanian/StringWars) - micro-benchmarking StringZilla against the best Rust tools
- [HashEvals](https://github.com/ashvardanian/HashEvals) - testing avalanche effect & differential patterns of string hash functions
- [ScalingElections](https://github.com/ashvardanian/ScalingElections) - parallel combinatorial voting in CUDA and Mojo for H100 GPUs
- [TinySemVer](https://github.com/ashvardanian/TinySemVer) - semantic versioning GitHub CI tool that doesn't take 300K lines of JavaScript
- [SwiftSemanticSearch](https://github.com/ashvardanian/SwiftSemanticSearch) - example of on-device real-time AI using UForm and USearch on iOS
- [ParallelReductionsBenchmark](https://github.com/ashvardanian/ParallelReductionsBenchmark) - GPGPU benchmarks for SyCL, CUDA, OpenCL, Vulkan, etc.
- [LibSee](https://github.com/ashvardanian/libsee) - non-intrusively profiling LibC calls with `LD_PRELOAD` tricks
- [PyBindToGPUs](https://github.com/ashvardanian/PyBindToGPUs) - C++ and CUDA starter kit for Python developers avoiding CMake
- [StringTape](https://github.com/ashvardanian/StringTape) - Apache Arrow compatible tapes for space-efficient string arrays
- [JaccardIndex](https://github.com/ashvardanian/JaccardIndex) - exploring CPU port utilization with Carry-Save Adders & Lookups
- [USearchBench.py](https://github.com/ashvardanian/USearchBench.py) - Billion-scale search benchmarks against FAISS, Weaviate, and Qdrant
- [USearchBench.java](https://github.com/ashvardanian/USearchBench.java) - Billion-scale search scaling benchmarks against Lucene, using Spark
- [ucsb](https://github.com/unum-cloud/ucsb) - parallel benchmarks for ACID-compliant key-value stores, like RocksDB
- [affine-gaps](https://github.com/gata-bio/affine-gaps) - "less wrong" local and global Gotoh sequence alignments in one NumBa Python file
- [faster-fasta](https://github.com/gata-bio/faster-fasta) - CLI tool for to parse, sort, dedup, and translate DNA, RNA, & protein sequences

## Materials

- [Tech Talks](https://ashvardanian.com/talks)
- [Personal Blog](https://ashvardanian.com/archives)
- [Corporate Blog](https://www.unum.cloud/blog)

Cherry picks:
[![](https://img.shields.io/youtube/views/bDRo7Cf7x1o?label=Matrix%20Multiplication%20Assembly%20Instructions%2C%202025)](https://www.youtube.com/watch?v=bDRo7Cf7x1o&list=PL2kcrNAeGTFzZbccNB3P_xruYPskMmwRT)
[![](https://img.shields.io/youtube/views/ybWeUf_hC7o?label=Designing%20the%20fastest%20ACID%20Key-Value%20Store%2C%202022)](https://www.youtube.com/watch?v=ybWeUf_hC7o&list=PL2kcrNAeGTFzZbccNB3P_xruYPskMmwRT)
[![](https://img.shields.io/youtube/views/AA4RI6o0h1U?label=Dive%20into%20the%20general%20purpose%20GPU%20programming%2C%202019)](https://www.youtube.com/watch?v=AA4RI6o0h1U&list=PL2kcrNAeGTFzZbccNB3P_xruYPskMmwRT)
[![](https://img.shields.io/youtube/views/PQKYc0zK0iU?label=Bird's%20Eye%20View%20of%20Open-Source%20AI%20Infrastructure%2C%202023)](https://www.youtube.com/watch?v=PQKYc0zK0iU&list=PL2kcrNAeGTFzZbccNB3P_xruYPskMmwRT&t=65s)
[![](https://img.shields.io/youtube/views/UMrhB3icP9w?label=Vector%20Search%20and%20Databases%20at%20Scale%2C%202023)](https://www.youtube.com/watch?v=UMrhB3icP9w&list=PL2kcrNAeGTFzZbccNB3P_xruYPskMmwRT&t=65s)
[![](https://img.shields.io/youtube/views/L9ELuU3GeNc?label=Fantastic%20Data%20Science%20Libraries%20and%20Where%20to%20Find%20Them%2C%202023)](https://www.youtube.com/watch?v=L9ELuU3GeNc&list=PL2kcrNAeGTFzZbccNB3P_xruYPskMmwRT)

