--1017223 rows
-- SELECT count(*)
-- FROM `sapient-duality-326917.trendingvideos161121.youtube_trending_videos`;

--Min date 2021-08-08 00:00:00 UTC
--No nulls in trending date
-- select trending_date, count(*)
-- FROM `sapient-duality-326917.trendingvideos161121.youtube_trending_videos`
-- group by trending_date
-- order by trending_date desc

--No Nulls
-- select category_name, count(*)
-- FROM `sapient-duality-326917.trendingvideos161121.youtube_trending_videos`
-- group by category_name
-- order by category_name desc

--No Nulls
-- select *
-- FROM `sapient-duality-326917.trendingvideos161121.youtube_trending_videos`
-- where likes is null
-- union all 
-- select *
-- FROM `sapient-duality-326917.trendingvideos161121.youtube_trending_videos`
-- where dislikes is null
-- union all
-- select *
-- FROM `sapient-duality-326917.trendingvideos161121.youtube_trending_videos`
-- where comment_count is null
-- union all
-- select *
-- FROM `sapient-duality-326917.trendingvideos161121.youtube_trending_videos`
-- where region is null

