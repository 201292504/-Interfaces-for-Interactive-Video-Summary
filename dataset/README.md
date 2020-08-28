### query_videoURLs.csv
This file contains queries and corresponding extracted videos (URLs) from YouTube.

### query_frame_annotations.csv
This file contains the URLs of the extracted video frames and the annotations of relevance and diversity for each frame from 5 different workers. Different annotations are uniquely identified by the assignment ID in the column 2.

## Dataset Annotation
We first annotate the video frames with query relevance labels, and then partition the frames into clusters according to visual similarity.
Relevance annotation ranges between 0 and 4 (Options for answers are “Trash”,“Not good”, “Good” and “Very Good”) for each frame.
Cluster annotations starts from 0 and ranges to an arbitary number. 0th cluster indicates Trash frames and are of low quality(e.g. blurred, bad contrast, etc.) while the cluster numbers >=1 indicates different groups. We obtain one clustering per worker, where each clustering consists of mutually exclusive subsets of video frames as clusters.
 
### query_videoURLs.csv
该文件包含查询以及从YouTube提取的相应视频（URL）。

### query_frame_annotations.csv
该文件包含提取的视频帧的URL以及来自5个不同工作者的每个帧的相关性和多样性的注释。不同的注释由第2列中的分配ID唯一标识。

##数据集注释
我们首先使用查询相关性标签注释视频帧，然后根据视觉相似性将帧划分为群集。
每个帧的相关性注释范围在0到4之间（答案选项为“废纸””，“不好”，“好”和“非常好”）。
群集注释从0开始，范围为任意数字。第0个群集表示垃圾桶，质量较低（例如模糊，对比度差等），而群集编号> = 1则表示不同的组。我们为每个工作人员获得一个群集，其中每个群集都由视频帧的互斥子集组成。