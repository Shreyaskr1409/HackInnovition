<script>
	import Button from "$lib/components/ui/button/button.svelte";

</script>
<div class="top-0 fixed justify-center items-center flex flex-col w-full h-20" id="navbar_top">
    <div class="mt-2 flex flex-row gap-5 px-5 items-center grow bg-zinc-900 h-full w-2/3 rounded-2xl">
        <div class="relative 2xl:bg-zinc-800 h-4 grow flex justify-center items-center">
            <div class=" bg-zinc-700 h-10 w-10 rounded-[2.5rem] 2xl:h-12 2xl:w-12 2xl:rounded-[3rem]"></div>
        </div>
        <Button class="w-28" variant="outline" href="http://localhost:5173/home">Home</Button>
        <Button class="w-28" variant="default" href="http://127.0.0.1:8000/fitness/">Fitness</Button>
        <Button class="w-28" variant="default" href="http://127.0.0.1:8000/health/">Mental Health</Button>
        <Button class="w-28" variant="default" href="http://127.0.0.1:8000/medication/">Medication</Button>
        <Button class="w-28" variant="default" href="http://127.0.0.1:8000/healthpredictor/">Health Predictor</Button>
        <Button class="w-28" variant="default" href="http://127.0.0.1:8000/nutrition/">Nutrition</Button>
        <Button class="w-28" variant="outline" href="http://127.0.0.1:8000/about/">About us</Button>
        <div class="relative 2xl:bg-zinc-800 h-4 grow flex justify-center items-center">
            <div class=" bg-zinc-700 h-10 w-10 rounded-[2.5rem] 2xl:h-12 2xl:w-12 2xl:rounded-[3rem]"></div>
        </div>
    </div>
</div>

<style>
    #navbar_top {
        filter: drop-shadow(0px 10px 10px #0000008f);
    }
</style>