<template lang="pug">
.wrapper  
  .content
    header
      img( src="https://i.scdn.co/image/05d3721739aee511a898081ab140daa7890a0120")
      .description
        span DARK POP,  ELECTRONICA,  LABORATORIO,  TRIP HOP
        .title
          h1 Portishead
          .title__icons
            .icons__pair
              img( src='~/assets/images/music_note_FILL0_wght400_GRAD0_opsz48.svg')
              span 27
            .icons__pair
              img( src='~/assets/images/album_FILL0_wght400_GRAD0_opsz48.svg')
              span 3
            .icons__pair
              img( src='~/assets/images/trending_up_FILL0_wght400_GRAD0_opsz48.svg')
              span 60
            img( src='~/assets/images/info_FILL0_wght400_GRAD0_opsz48.svg')
        p Portishead (/pɔːrtɪsˈhɛd/) are an English band formed in 1991 in Bristol. Portishead are named after Portishead, Somerset, eight miles west of Bristol, along the coast. The band comprises vocalist Beth Gibbons, producer Geoff Barrow, and musician Adrian Utley; Dave McDonald, an engineer on their first records, is sometimes cited as the fourth member.

</template>

<script>
export default {
  
}
</script>

<style lang="scss" scoped>
.wrapper {
  > .content {
    width: 90%;
    margin: 0 auto;
    > header {
      display: flex;
      align-items: center;
      > img {
        width: 240px;
        height: 240px;
        object-fit: cover;
        border-radius: 20px;
      }
      > .description {
        > span {
          font: 400 14px 'Lato';  
          color: #AEAEAE;
          margin-left: 16px;
        }
        > .title {
          width: 100%;
          display: flex;
          justify-content: space-between;
          > h1 {
            margin-left: 8px;
          }
          > .title__icons {
            display: flex;
            align-self: start;
            margin-top: 16px;
            // grid-template-colum
            & img {
              width: 26px;
              height: 26px;
              margin-left: 16px;
            }
            & span {
              font: normal 18px 'Lato';
              color: #E3E3E3;
              margin-left: 2px;
            }
            > .icons__pair {
              display: flex;
              align-items: center;
            }
          }
        }
        > p {
          margin-left: 16px;
        }
      }
    }
  }
}
</style>