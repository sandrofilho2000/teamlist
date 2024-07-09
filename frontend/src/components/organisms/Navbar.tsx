'use client';

import { useSystem } from '@context/useSystem';
import React from 'react';
import { GiSoccerBall } from 'react-icons/gi';
import { IoMdFootball } from 'react-icons/io';
import { MdOutlineMenu } from 'react-icons/md';

const Navbar = () => {
  const { isAsideOpen, setIsAsideOpen }: any = useSystem();
  return (
    <nav className="background-color flex text-white  justify-between items-center  bg-[#141414] fixed w-screen left-0 z-40 h-[50px] px-4 transition ease-in-out delay-150 shadow-[7px_6px_10px_0px_#00000024]">
      <MdOutlineMenu
        onClick={() => {
          setIsAsideOpen(!isAsideOpen);
        }}
        className="text-[40px] cursor-pointer "
      />
      <h1 className="m-auto absolute left-[50%] -translate-x-[50%] text-2xl font-bold">
        <a
          href="/"
          className="mb-0 flex items-center gap-1 whitespace-nowrap"
        >
          <GiSoccerBall />
          TEAMS LIST
        </a>
      </h1>

      {/* {% include 'atomic/organisms/datalist_desktop.html' %}
        {% include 'atomic/organisms/datalist_mobile.html' %} */}
    </nav>
  );
};

export default Navbar;
