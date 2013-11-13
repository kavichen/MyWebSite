<?php get_header(); ?>
 <?php if (function_exists('pagenavi')) { pagenavi(); } ?>
    <div id="content">
        <div id="main-content">
        <?php query_posts("cat=-100,-101,-102&paged=$paged")?><?php if (have_posts()) : ?>
            <?php while (have_posts()) : the_post(); ?>
                <div class="post" id="post-<?php the_ID(); ?>">
                    <h1><a href="<?php the_permalink() ?>" rel="bookmark" title="<?php the_title(); ?>"><?php the_title(); ?></a></h1>
                    <span class="date">by <?php the_author(); ?> on <?php the_time(__('m/j/Y','min')) ?></span>
                    <div class="clearfix"></div>
                    <div class="entry">
                        <?php the_content(__('Continue Reading','min').' &raquo;'); ?>
                    </div>
                    <span class="number-of-comments"><a href="<?php the_permalink() ?>#comments"><?php comments_number(__('No Comments','min'), __('1 Comment','min'), __('% Comments','min'));?></a></span>
                </div><!-- close:post -->
            <?php endwhile; ?>
            <div class="pagination clearfix">
                <?php if(function_exists('wp_page_numbers')) { wp_page_numbers(); }; ?>
            </div>
        <?php else : ?>
            <p class="string"><?php _e('You broke the interwebs... wow... way to go.. no really you may want to call someone to take a look at it..','min'); ?></p>
            <a href="<?php echo get_option('home'); ?>/" class="back"><?php _e('Back home','min'); ?></a>
        <?php endif; ?>
        </div><!-- close:main-content -->
        <?php get_sidebar(); ?>
    </div><!-- close:content -->
<?php get_footer(); ?>
