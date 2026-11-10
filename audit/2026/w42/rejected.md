# W42 rejected / not selected (search 2026-10-26; OpenAlex re-run 2026-10-28 after rate-limit reset, no new selectable item)

Public keywords only. Dedup done against nand-ops/used_sources.md (W40, W43, W44 reserved), origin/main audit+reports+knowledge, and branches reliability-w41/w42/w43, weekly/2026-w40, weekly/2026-w43. W41's five (10.1007/s10825-026-02647-9, arXiv 2610.06173, 2610.11643, 10.1007/s44275-026-00054-7, 10.1142/s0217984926502520) and W44 reserved DOIs were not taken.

| Item | Why not selected |
|---|---|
| arXiv 2610.06363 (HZO STEM-EBIC) | draft-branch hint; v1 submitted 2026-10-05 = W41 window; off-topic |
| 10.1109/LED.2026.3710382 (cryo 3D NAND retention) | draft hint; issue 2026-09, no day-level date; closed, no abstract -> metadata_only |
| 10.1109/TED.2026.3724518 (PINN PGM 3-D CT-NAND) | draft hint; month-only date (2026-10), closed, metadata_only |
| 10.1109/TPEL.2026.3710070 (SiC oxide traps) | draft hint; issue 2026-11, closed; not VNAND |
| 10.1109/TED.2026.3741484 (hole trapping in SiN, dynamic CV) | VNAND-relevant, but Crossref only 'created 2026-10-16'; OpenAlex date is a 2026-01-01 placeholder; IEEE page JS-only; closed. Date UNKNOWN. Worth a retry if user has access |
| IEEE TDMR/EDL/TED/JEDS early-access items; Elsevier 10.1016/j.microrel.2026.116327 (SiC avalanche after H3TRB) etc. | Crossref gives issue month only; online day unverifiable; closed. Elsevier not scraped (403 policy) |
| 10.3390/electronics15204733 (BIST, embedded flash test), 10.3390/nano16201294 (SiO2/HfOxNy MISFET), 10.3390/electronics15204744 (IGBT RUL) | in window, but mdpi.com HTTP 403; not in Europe PMC; no abstract read -> not usable |
| 10.1088/1361-6463/aeb4c5 (SiC MOSFET vs Si-IGBT TCAD reliability), aeb30b (UTB DG interface traps) | in window; IOP shows abstract only to automation (aeb4c5: received 3 Jul, accepted 15 Oct 2026); would be abstract_only; overlaps W43 SiC topic; held as reserve |
| 10.1002/smll.76242 (NAND-compatible FE memcapacitor), 10.1002/pssa.70553 (cylindrical GAA TFET traps) | Wiley HTTP 403; neuromorphic / TFET design, weak reliability physics |
| 10.3389/fnano.2026.1961029, 10.1063/5.0355163 | in window but already used by W43 (dedup) |
| 10.56557/ajocr/2026/v11i411227 (GaN dynamic Ron, charge trapping) | low-quality venue, not read |
| Authorea 10.22541/authorea.15010563/v1 (WSe2 FE memory with charge trapping, 2026-10-15) | preprint repository, 2D channel, not read; reserve only |
| Mendeley 10.17632/nkxp7ntkp2 (TCAD data poly-Si TFT grains, 2026-10-16) | dataset not paper; not read; possible follow-up for poly-Si channel |
| arXiv 2610.22418 (Skipper-CCD charge traps) | off-topic |
| arXiv 2610.16255 (IGZO memory), 2610.19697 (FeFET CIM), 2610.26960 (VS-Flash) | memory-system / device statistics, not reliability physics; not read |
| arXiv 2608.14073 (read disturbance in 15 SSDs) | archive_gap reserve, abstract read only; system-level |
| arXiv 2608.09622 (MCTS reliability test planning) | read in full (fulltext_notes_W42-R1.md); simulation-only, not VNAND -> reserve |
| 10.1063/5.0348039, 5.0354396, 5.0323691 (Ga2O3 / SiC irradiation) | off-topic for this week's focus |

Access failures (not bypassed): mdpi.com (eng7100563, electronics, nano) 403; onlinelibrary.wiley.com 403; iopscience full body not exposed; ieeexplore document page returned no text.
Coverage caveat: OpenAlex first run hit HTTP 429 (partial); re-run 2026-10-28 completed. In-window GIDL/CTL-retention-specific and Weibull/HV SOA-specific readable sources: none found (UNKNOWN whether absent).
